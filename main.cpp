#include "bmp.hpp"

#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

const unsigned HEIGHT=8;

int main(int argc, char** argv){
	if(argc!=2) return -1;
	ifstream file(argv[1]);
	vector<vector<BmpColor> > pixels;
	pixels.push_back(vector<BmpColor>());
	string rChannel, gChannel, bChannel;
	while(file.good()){
		if(pixels.back().size()==HEIGHT) pixels.push_back(vector<BmpColor>());
		int x;
		file>>hex>>x;
		if(!file.good()) break;
		pixels.back().push_back(BmpColor(x&0xff, (x&0xff00)>>8, (x&0xff0000)>>16));
		rChannel+=x&0xff;
		gChannel+=(x&0xff00)>>8;
		bChannel+=(x&0xff0000)>>16;
	}
	writeBmp("result.bmp", pixels);
	ofstream text("result.txt");
	text<<rChannel<<"\n\n----------\n\n";
	text<<gChannel<<"\n\n----------\n\n";
	text<<bChannel<<"\n\n----------\n\n";
	for(unsigned i=0; i<gChannel.size(); ++i)
		gChannel[i]+=' '-'+';
	text<<gChannel<<"\n\n----------\n\n";
	for(unsigned i=0; i<gChannel.size(); ++i)
		switch((unsigned char)gChannel[i]){
			case 'G': gChannel[i]='Y'; break;
			case 'Y': gChannel[i]='o'; break;
			case 's': gChannel[i]='u'; break;
			case 'U': gChannel[i]='k'; break;
			case 'Z': gChannel[i]='n'; break;
			case 'q': gChannel[i]='w'; break;
			case 0x1c: gChannel[i]=','; break;
			case '7': gChannel[i]='I'; break;
			case 'X': gChannel[i]='h'; break;
			case '_': gChannel[i]='a'; break;
			case 'r': gChannel[i]='v'; break;
			case 'c': gChannel[i]='e'; break;
			case 'b': gChannel[i]='f'; break;
			case '^': gChannel[i]='b'; break;
			case 'm': gChannel[i]='s'; break;
			case 'Q': gChannel[i]='w'; break;
			case 'W': gChannel[i]='i'; break;
			case ']': gChannel[i]='c'; break;
			case 0x8e: gChannel[i]='\''; break;
			case 'n': gChannel[i]='r'; break;
			case 'g': gChannel[i]='y'; break;
			case ')': gChannel[i]='?'; break;
			case '\\': gChannel[i]='l'; break;
			case 0x1a: gChannel[i]='.'; break;
			case 'a': gChannel[i]='g'; break;
			case '[': gChannel[i]='m'; break;
			case '?': gChannel[i]='A'; break;
			case 'h': gChannel[i]='x'; break;
			case ':': gChannel[i]='N'; break;
			case 'V': gChannel[i]='j'; break;
			case 'I': gChannel[i]='_'; break;
			case ';': gChannel[i]='M'; break;
			case 0x1b: gChannel[i]='-'; break;
			case 'o': gChannel[i]='q'; break;
			case 'O': gChannel[i]='Q'; break;
			case '>': gChannel[i]='B'; break;
			case '8': gChannel[i]='H'; break;
			case '%': gChannel[i]=';'; break;
			default: break;
		}
	text<<gChannel<<"\n\n----------\n\n";//overall this is just xored with 0xb
	text.close();
	vector<vector<BmpColor> > channeled;
	channeled.resize(pixels.size());
	//---red---//
	ofstream listr("listr.txt");
	for(unsigned i=0; i<pixels.size(); ++i){
		channeled[i].resize(pixels[0].size());
		for(unsigned j=0; j<pixels[0].size(); ++j){
			channeled[i][j]=BmpColor(pixels[i][j].r, 0, 0);
			listr<<(unsigned)pixels[i][j].r<<",";
		}
	}
	writeBmp("r.bmp", channeled);
	listr.close();
	//---green---//
	for(unsigned i=0; i<pixels.size(); ++i){
		channeled[i].resize(pixels[0].size());
		for(unsigned j=0; j<pixels[0].size(); ++j)
			channeled[i][j]=BmpColor(0, pixels[i][j].g, 0);
	}
	writeBmp("g.bmp", channeled);
	//---blue---//
	ofstream listb("listb.txt");
	for(unsigned i=0; i<pixels.size(); ++i){
		channeled[i].resize(pixels[0].size());
		for(unsigned j=0; j<pixels[0].size(); ++j){
			channeled[i][j]=BmpColor(0, 0, pixels[i][j].b);
			listb<<(unsigned)pixels[i][j].b<<",";
		}
	}
	writeBmp("b.bmp", channeled);
	listb.close();
	//---random---//
	ofstream listrandom("listrandom.txt");
	for(unsigned i=0; i<pixels.size(); ++i){
		channeled[i].resize(pixels[0].size());
		for(unsigned j=0; j<pixels[0].size(); ++j){
			channeled[i][j]=BmpColor(rand()%0x100, 0, 0);
			listrandom<<(unsigned)channeled[i][j].r<<",";
		}
	}
	writeBmp("random.bmp", channeled);
	listrandom.close();
	return 0;
}
