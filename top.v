module top(CLK,PIN_1,PIN_2,PIN_3,PIN_4,PIN_5,PIN_6,PIN_7,PIN_8,PIN_9,PIN_10,USBPU);

input CLK; //16mhz master clock

output PIN_1; //hsync
output PIN_2; //vsync

output PIN_3; //red   0 lsb
output PIN_4; //red   1
output PIN_5; //red   2 msb
output PIN_6; //green 3 lsb
output PIN_7; //green 4
output PIN_8; //green 5 msb
output PIN_9; //blue  6 lsb
output PIN_10;//blue  7 msb

output USBPU; //usb pullup aaaaaaa
assign USBPU = 0;

wire pclk; //pixel clock

reg [9:0] hcount; //horizontal pixel counter
reg [8:0] vcount; //vertical line counter

reg hblank;
reg vblank; //blanking intervals

reg hsync;
reg vsync; //sync pulses

reg [7:0] vbuf [79:0][59:0]; //video buffer
reg [7:0] pixel; //current pixel

//shove an image into the video buffer
initial begin
	$readmemh("pic.txt",vbuf);
end

//pll configuration for 36mhz pixel clock
SB_PLL40_CORE#(
		.FEEDBACK_PATH("SIMPLE"),
		.DIVR(4'b0000),
		.DIVF(7'b0001000),
		.DIVQ(3'b010),
		.FILTER_RANGE(3'b001)
	)uut(
		.BYPASS(1'b0),
		.REFERENCECLK(CLK),
		.PLLOUTCORE(pclk),
		.RESETB(1'b1)
		);

always @(posedge pclk)begin
	
	//counting + blanking intervals
	hcount <= hcount + 1;
	if(hcount==10'd832)begin
		hcount <= 0;
		vcount <= vcount + 1;
		hblank <= 1'b1;
	end
	if(vcount==9'd509)begin
		vcount <= 0;
		vblank <= 1'b1;
	end
	if(hcount==10'd640)begin
		hblank <= 1'b0;
	end
	if(vcount==9'd480)begin
		vblank <= 1'b0;
	end
	
	//sync pulses
	if(hcount==10'd696)begin
		hsync <= 1'b0;
	end
	if(hcount==10'd752)begin
		hsync <= 1'b1;
	end
	if(vcount==9'd481)begin
		vsync <= 1'b0;
	end
	if(vcount==9'd484)begin
		vsync <= 1'b1;
	end
	
	//get pixel
	if (hblank && vblank)begin
		pixel <= vbuf[hcount[9:2]][vcount[8:2]];
	end else begin
		pixel <= 8'b0;
	end
	
end

assign PIN_1 = hsync;
assign PIN_2 = vsync;

assign PIN_3  = pixel[0];
assign PIN_4  = pixel[1];
assign PIN_5  = pixel[2];
assign PIN_6  = pixel[3];
assign PIN_7  = pixel[4];
assign PIN_8  = pixel[5];
assign PIN_9  = pixel[6];
assign PIN_10 = pixel[7];

endmodule
