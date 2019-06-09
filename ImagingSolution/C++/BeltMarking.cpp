#include <windows.h>
#include <iostream>
#include <winsock.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <math.h>
#include "opencv/cv.h"
#include "opencv2/opencv.hpp"
#include "opencv2/highgui.hpp"

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/calib3d/calib3d.hpp>
#include <vector>
#include <iostream>
#include <fstream>

#define NO_FLAGS_SET 0

#define MAXBUFLEN 512

#define M_PI 3.14159265359

#define QR_CODE_NUM 10
#define SERVO_NUM 6

#define CAMERA_WIDTH 640
#define CAMERA_HEIGHT 480

using namespace std;
using namespace cv;

double start, fin, Nowtime;

int VF_Last = 0;

int fin_count = 0;

bool drawing_box = false;

Point targetPoint;
Point2f Red_Point;// Clicked pixels(Camera1)


Mat src_img;			 // Camera1 Color Image (Current)
Mat prev_src_img;		 // Camera1 Color Image (Before 1 loop)

Mat src2_img;			// Camera2 Color Image (Current)
Mat prev_src2_img;		// Camera2 Color Image (Before 1 loop)

Mat src3_img;			// Camera3 Color Image (Current)
Mat prev_src3_img;		// Camera3 Color Image (Before 1 loop)

FILE *fp1;// Output File

char key = '@';

int control_status = 99;

Mat result_img0;
Mat hsv_img0, hsv_img1;
Mat gray_img0, gray_img1;
Mat bin_img0, bin_img1;
Mat adaptivenoisefilter;
Point2d point0, point1;

std::vector<cv::Mat> planes;
std::vector<cv::Mat> planes2;

cv::Mat imgThreshold_R;
cv::Mat imgThreshold_G;
cv::Mat imgThreshold_B;
cv::Mat imgResult = Mat(CAMERA_WIDTH, CAMERA_HEIGHT, CV_8UC1);
cv::Mat imgTmp;
cv::Mat markColor;

unsigned long counter = 0;
int loop = 1;
int disp = 0;
int disp_data = 0;
int ch;
int mkr1HSV[4] = { 0, 10, 50, 50 };//ê‘

Point preTarget;

Point GetGrabPoint(Mat a1)
{
	a1;
	Point target;
	Point temp;
	target.x = 0;
	target.y = 0;
	preTarget.x = CAMERA_WIDTH;
	preTarget.y = CAMERA_HEIGHT;

	unsigned char p;

	for (int y = CAMERA_HEIGHT; y > 0; y--){
		for (int x = CAMERA_WIDTH; x > 0; x--){
			p = a1.at<uchar>(y, x);
			if (p == 255 && x < preTarget.x && y < preTarget.y){
				if (fabs(y - preTarget.y) > 20){
					if (fabs(x - preTarget.x) > 10) {
						temp.x = x;
						temp.y = y;
						preTarget.x = x;
						preTarget.y = y;
					}
					else {
						temp.x = preTarget.x;
						temp.y = preTarget.y;
					}
				}
				else {
					temp.x = x;
					temp.y = y;
					preTarget.x = x;
					preTarget.y = y;
				}
			}
			else{
				temp.x = preTarget.x;
				temp.y = preTarget.y;
			}
		}
	}
	target.x = temp.x;
	target.y = temp.y;
	return target;
}

INT main(VOID) {
	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™
	//		Variable setting
	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™

	float input[6] = { (float)0.0 };
	float delta[6] = { (float)0.0 };
	long ratio = 1;
	float receive_data[4][SERVO_NUM] = { (float)0.0 };

	fopen_s(&fp1, "170130.csv", "w");
	fprintf(fp1, "time[s],tmp_diff[0],tmp_diff[1],tmp_diff[2],tmp_diff[3],tmp_diff[4],tmp_diff[5]\n");

	VideoCapture cap_1(0);			 // Capture of Camera1

	cv::Mat prev_src_img;
	cv::Size frameSize = prev_src_img.size();
	cap_1 >> prev_src_img;			// First Flame Setting (Camera1)

	cv::waitKey(10);


	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™
	//		Control loop
	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™
	while (loop) {

		result_img0 = Scalar(0, 0, 0);

		cap_1 >> src_img;							//Caputure Camera1				
													//Center Point
		key = (char)waitKey(10);
		if (key == 27) { break; }


		cv::medianBlur(src_img, src_img, 3);	//ÉmÉCÉYÇ™Ç†ÇÈÇÃÇ≈ïΩääâª

		cv::split(src_img, planes);
		cv::threshold(planes[2], imgThreshold_R, 100, 255, CV_THRESH_BINARY);
		imgTmp = planes[2] / planes[1];
		imgTmp = imgTmp * 10;
		cv::threshold(imgTmp, imgThreshold_G, 15, 255, CV_THRESH_BINARY);
		imgTmp = planes[2] / planes[0];
		imgTmp = imgTmp * 10;
		cv::threshold(imgTmp, imgThreshold_B, 15, 255, CV_THRESH_BINARY);
		bitwise_and(imgThreshold_G, imgThreshold_B, imgTmp);
		bitwise_and(imgTmp, imgThreshold_R, imgResult);

		//îcéùì_éÊìæ
		targetPoint = GetGrabPoint(imgResult);

		cout << "x = " << targetPoint.x << ","
			 << "y = " << targetPoint.y << endl;


	    // Paint Point
		circle(src_img, targetPoint, 3, Scalar(0, 255, 0), -1, 10, 0);

		imshow("Image", src_img); // Screen display (Camera1)
		imshow("Result", imgResult); // Screen display (Camera1)
	}
	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™
	//		End processing
	//Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™Ñ™

	// End
	cout << "/// End /// " << endl;
	return 0;
}