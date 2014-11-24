#ifndef _BMP_HPP_INCLUDED
#define _BMP_HPP_INCLUDED

#include <string>
#include <vector>

struct BmpColor{
	BmpColor(){}
	BmpColor(unsigned char r, unsigned char g, unsigned char b): r(r), g(g), b(b){}
	unsigned char r, g, b;
};

void readBmp(std::string fileName, std::vector<std::vector<BmpColor> >& pixels);
void writeBmp(std::string fileName, std::vector<std::vector<BmpColor> >& pixels);

#endif
