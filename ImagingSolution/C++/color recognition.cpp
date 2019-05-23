#include	<iostream>
#include    <vector>
#include    <opencv2/highgui/highgui.hpp>
#include	<opencv2/imgproc/imgproc.hpp>

#define WIDTH 800
#define HEIGHT 600
#define WINDOWNAME1 "Real Image"
#define WINDOWNAME2 "HSV Image"
#define WINDOWNAME3 "Masked Image"
#define WINDOWNAME4 "Output Image"

using namespace std;
using namespace cv;


int main(void)
{
	VideoCapture vc;		//�L���v�`���p�ϐ�

	//�t���[���T�C�Y��`
	vc.set(CV_CAP_PROP_FRAME_WIDTH, WIDTH);
	vc.set(CV_CAP_PROP_FRAME_HEIGHT, HEIGHT);

	//�h���C�o�[�̈�
	Point2f p1(180, 350);	//�g������W
	Point2f p2(450, 550);	//�g��E�����W
	size_t driver_area = (450 - 180) * (550 - 350);

	//�r�b�g����̈�
	Point2f p3(240, 250);	//�g������W
	Point2f p4(380, 330);	//�g��E�����W
	size_t bit_area = (380 - 240) * (330 - 250);

	const Scalar color(0, 0, 255);	//�g�F�ݒ�(BGR)

	Mat img, scr, smooth_img, bin_image;
	Mat hsv_image, output_image;
	Mat mask_image = Mat(HEIGHT, WIDTH, CV_8UC1);		//2�l���p�̃E�C���h�E�쐬

	int cercle_num = 0;
	int key_input = 0;

	int gX;
	int gY;


	unsigned char p;

	float  BitSize = (380 - 240) * (330 - 250);
	float  DareaSize = (450 - 180) * (550 - 350);
	float  Bjudge = 0;
	float  Djudge = 0;
	float  Djudge_num = 0;
	float  Bjudge_num = 0;


	//-----------------(HSV�F���f�[�^)-------------------------
	int mkOHSV[6] = { 140, 190, 180, 230, 100, 255 };//�I�����W
	int mkRHSV[6] = { 140, 190, 180, 230, 100, 255 };//�ԐF�}�[�J
	int mkBHSV[6] = { 100, 140, 40, 255, 50, 255 };//�F�}�[�J
	int mkGHSV[6] = { 50, 80, 40, 255, 50, 255 };//�F�}�[�J
	//--------------------------------------------------------

	vector<vector<Point> > contours;
	vc.open(0);
	if (!vc.isOpened())
	{
		cout << "Can not open camera." << endl;

		vc.release();
		return -1;
	}

	cout << "���������Ȃ�G���^�[�L�[����͂����Ă�������" << endl;

	while (1)
	{
		vc >> img;

		cercle_num = 0;

		cv::namedWindow(WINDOWNAME1, CV_WINDOW_AUTOSIZE);

		//�m�C�Y������̂ŕ�����
		cv::medianBlur(img, smooth_img, 9);
		//BGR����HSV�ɕϊ�
		cv::cvtColor(smooth_img, hsv_image, CV_BGR2HSV);
		cv::namedWindow(WINDOWNAME2, CV_WINDOW_AUTOSIZE);

		// inRange��p���ăt�B���^�����O
		Scalar s_min = Scalar(30, 100, 20);
		Scalar s_max = Scalar(70, 255, 255);
		cv::inRange(hsv_image, s_min, s_max, mask_image);
		namedWindow(WINDOWNAME3, CV_WINDOW_AUTOSIZE);

		//�̈�\��
		cv::rectangle(img, p1, p2, color, 4);
		cv::rectangle(img, p3, p4, color, 4);

		//�o��
		cv::imshow(WINDOWNAME2, hsv_image);
		cv::imshow(WINDOWNAME3, mask_image);
		cv::imshow(WINDOWNAME4, img);

		int key = cv::waitKey(1);

		if (key == 113) {	//"q"���͂�break
			break;
		}

		else if (key == 115) {		////"s"���͂Ŕ���
			for (int area = 0; area <= 1; area++) {
				if (area == 0) {
					for (int y = 350; y <= 550; y++) {
						for (int x = 180; x <= 450; x++) {
							p = mask_image.at<uchar>(y, x);
							if (p == 255) {
								Djudge_num += 1;
							}
						}
					}
				}
				else if (area == 1) {
					for (int y = 250; y <= 330; y++) {
						for (int x = 240; x <= 380; x++) {
							p = mask_image.at<uchar>(y, x);
							if (p == 255) {
								Bjudge_num += 1;
							}
						}
					}
				}
			}

			Djudge = (Djudge_num / DareaSize) * 100;
			Bjudge = (Bjudge_num / BitSize) * 100;

			if (Bjudge > 30) {
				cout << "D = " << Djudge << "," << "B = " << Bjudge << endl;
				cout << "Bit is inserted." << endl;
				Djudge_num = 0;
				Bjudge_num = 0;
				Bjudge = 0;
				Djudge = 0;
			}

			else {
				cout << "D = " << Djudge << "," << "B = " << Bjudge << endl;
				cout << "Bit is not inserted." << endl;
				Djudge_num = 0;
				Bjudge_num = 0;
				Bjudge = 0;
				Djudge = 0;
			}

		}
	
	}
	return 0;
}














