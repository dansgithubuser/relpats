#include "bmp.hpp"

#include <fstream>

using namespace std;

//-----helpers-----//
static void write(unsigned x, ofstream& file, unsigned size){
	for(unsigned i=0; i<size; ++i){
		file.put(x%0x100);
		x>>=8;
	}
}

static unsigned read(ifstream& file, unsigned size){
	unsigned result=0;
	for(unsigned i=0; i<size; ++i)
		result|=file.get()<<(i*8);
	return result;
}

static void read24BitBmpData(ifstream& file, vector<vector<BmpColor> >& data){
	if(data.size()==0||data[0].size()==0) return;
	for(unsigned y=0; y<data[0].size(); ++y){
		for(unsigned x=0; x<data.size(); ++x){
			data[x][y].b=file.get();
			data[x][y].g=file.get();
			data[x][y].r=file.get();
		}
		for(unsigned j=0; j<(4-((3*data.size())%4))%4; ++j) file.get();
	}
}

static void write24BitBmpData(ofstream& file, vector<vector<BmpColor> >& data){
	if(data.size()==0||data[0].size()==0) return;
	for(unsigned y=0; y<data[0].size(); ++y){
		for(unsigned x=0; x<data.size(); ++x){
			file.put(data[x][y].b);
			file.put(data[x][y].g);
			file.put(data[x][y].r);
		}
	for(unsigned j=0; j<(4-((3*data.size())%4))%4; ++j) file.put(0);
	}
}

static void readBmpHeader(
	ifstream& file,
	unsigned short& type,
	unsigned& fileSize,
	unsigned short& reserved1,
	unsigned short& reserved2,
	unsigned& offset
){
	type=read(file, 2);
	fileSize=read(file, 4);
	reserved1=read(file, 2);
	reserved2=read(file, 2);
	offset=read(file, 4);
}

static void writeBmpHeader(
	ofstream& file,
	unsigned short type,
	unsigned fileSize,
	unsigned short reserved1,
	unsigned short reserved2,
	unsigned offset
){
	write(type, file, 2);
	write(fileSize, file, 4);
	write(reserved1, file, 2);
	write(reserved2, file, 2);
	write(offset, file, 4);
}

static void readDibHeader(
	ifstream& file,
	int& width,
	int& height, 
	unsigned short& bitsPerPixel,
	unsigned& compression,
	unsigned& size,
	unsigned& horizontalPixelsPerMeter,
	unsigned& verticalPixelsPerMeter,
	unsigned& colorsUsed,
	unsigned& importantColors
){
	unsigned headerSize=read(file, 4);//header size, always 40
	if(headerSize!=40) return;
	width=read(file, 4);
	height=read(file, 4);
	unsigned colorPlanes=read(file, 2);//number of color planes -- must be 1
	if(colorPlanes!=1) return;
	bitsPerPixel=read(file, 2);
	compression=read(file, 4);
	size=read(file, 4);
	horizontalPixelsPerMeter=read(file, 4);
	verticalPixelsPerMeter=read(file, 4);
	colorsUsed=read(file, 4);
	importantColors=read(file, 4);
}

static void writeDibHeader(
	ofstream& file,
	int width,
	int height,
	unsigned short bitsPerPixel,
	unsigned compression,
	unsigned size,
	unsigned horizontalPixelsPerMeter,
	unsigned verticalPixelsPerMeter,
	unsigned colorsUsed,
	unsigned importantColors
){
	write(40, file, 4);
	write(width, file, 4);
	write(height, file, 4);
	write(1, file, 2); 
	write(bitsPerPixel, file, 2);
	write(compression, file, 4);
	write(size, file, 4);
	write(horizontalPixelsPerMeter, file, 4);
	write(verticalPixelsPerMeter, file, 4);
	write(colorsUsed, file, 4);
	write(importantColors, file, 4);
	return;
}

//-----functions-----//
void readBmp(string fileName, vector<vector<BmpColor> >& pixels){
	ifstream file;
	file.open(fileName.c_str(), ifstream::in|ifstream::binary);
	unsigned short type;
	unsigned fileSize;
	unsigned short reserved1;
	unsigned short reserved2;
	unsigned offset;
	readBmpHeader(file, type, fileSize, reserved1, reserved2, offset);
	if(type!=('B'|('M'<<8))) return;
	int width;
	int height;
	unsigned short bitsPerPixel;
	unsigned compression;
	unsigned size;
	unsigned horizontalPixelsPerMeter;
	unsigned verticalPixelsPerMeter;
	unsigned colorsUsed;
	unsigned importantColors;
	readDibHeader(file, width, height, bitsPerPixel, compression, size,
		horizontalPixelsPerMeter, verticalPixelsPerMeter, colorsUsed,
		importantColors);
	if(bitsPerPixel!=24) return;
	if(colorsUsed!=0) return;
	pixels.resize(width);
	for(unsigned i=0; i<pixels.size(); ++i)
		pixels[i].resize(height);
	read24BitBmpData(file, pixels);
	file.close();
}

void writeBmp(string fileName, vector<vector<BmpColor> >& pixels){
	if(pixels.size()==0||pixels[0].size()==0) return;
	ofstream file;
	file.open(fileName.c_str(), ofstream::out|ofstream::binary);
	writeBmpHeader(
		file,
		'B'|('M'<<8),
		54+(3*pixels.size()+((4-((3*pixels.size())%4))%4))*pixels[0].size(),
		0,
		0,
		54);
	writeDibHeader(
		file,
		pixels.size(),
		pixels[0].size(),
		24,
		0,
		0,//usual value for uncompressed files
		0,
		0,
		0,//which means default 2^n, ie 2^24
		0);//usually ignored
	write24BitBmpData(file, pixels);
	file.close();
}
