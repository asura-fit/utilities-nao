/**********************************************
/     uyuv to yuv converter
/
/                                author: sin
/
/*********************************************/

#include <stdio.h>
#include <unistd.h>
#include <assert.h>

#define NUM_YUYV 4
#define NUM_YUV 3


int main(void) {
	int n;
	char ibuf[NUM_YUYV];
	char opx1[NUM_YUV];
	char opx2[NUM_YUV];

	char u, y1, v, y2;

	do {
		//read from pipe(stdin) to inbuf
		n = fread(ibuf, sizeof(char), NUM_YUYV, stdin);
		if (n == 0) 
			break;
		assert(n == NUM_YUYV);

		y1 = ibuf[0];
		v = ibuf[1];
		y2 = ibuf[2];
		u = ibuf[3];

		opx1[0] = y1;
		opx1[1] = u;
		opx1[2] = v;
		opx2[0] = y2;
		opx2[1] = u;
		opx2[2] = v;

		//write to pipe(stdout) from outbuf
		fwrite(opx1, sizeof(char), NUM_YUV, stdout);
		fwrite(opx2, sizeof(char), NUM_YUV, stdout);
	} while (1);

	return 0;
}
