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
	VideoCapture vc;		//キャプチャ用変数

	//フレームサイズ定義
	vc.set(CV_CAP_PROP_FRAME_WIDTH, WIDTH);
	vc.set(CV_CAP_PROP_FRAME_HEIGHT, HEIGHT);

	//ドライバー領域
	Point2f p1(180, 350);	//枠左上座標
	Point2f p2(450, 550);	//枠上右下座標
	size_t driver_area = (450 - 180) * (550 - 350);

	//ビット判定領域
	Point2f p3(240, 250);	//枠左上座標
	Point2f p4(380, 330);	//枠上右下座標
	size_t bit_area = (380 - 240) * (330 - 250);

	const Scalar color(0, 0, 255);	//枠色設定(BGR)

	Mat img, scr, smooth_img, bin_image;
	Mat hsv_image, output_image;
	Mat mask_image = Mat(HEIGHT, WIDTH, CV_8UC1);		//2値化用のウインドウ作成

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


	//-----------------(HSV色相データ)-------------------------
	int mkOHSV[6] = { 140, 190, 180, 230, 100, 255 };//オレンジ
	int mkRHSV[6] = { 140, 190, 180, 230, 100, 255 };//赤色マーカ
	int mkBHSV[6] = { 100, 140, 40, 255, 50, 255 };//青色マーカ
	int mkGHSV[6] = { 50, 80, 40, 255, 50, 255 };//青色マーカ
	//--------------------------------------------------------

	vector<vector<Point> > contours;
	vc.open(0);
	if (!vc.isOpened())
	{
		cout << "Can not open camera." << endl;

		vc.release();
		return -1;
	}

	cout << "判定をするならエンターキーを入力をしてください" << endl;

	while (1)
	{
		vc >> img;

		cercle_num = 0;

		cv::namedWindow(WINDOWNAME1, CV_WINDOW_AUTOSIZE);

		//ノイズがあるので平滑化
		cv::medianBlur(img, smooth_img, 9);
		//BGRからHSVに変換
		cv::cvtColor(smooth_img, hsv_image, CV_BGR2HSV);
		cv::namedWindow(WINDOWNAME2, CV_WINDOW_AUTOSIZE);

		// inRangeを用いてフィルタリング
		Scalar s_min = Scalar(30, 100, 20);
		Scalar s_max = Scalar(70, 255, 255);
		cv::inRange(hsv_image, s_min, s_max, mask_image);
		namedWindow(WINDOWNAME3, CV_WINDOW_AUTOSIZE);

		//領域表示
		cv::rectangle(img, p1, p2, color, 4);
		cv::rectangle(img, p3, p4, color, 4);

		//出力
		cv::imshow(WINDOWNAME2, hsv_image);
		cv::imshow(WINDOWNAME3, mask_image);
		cv::imshow(WINDOWNAME4, img);

		int key = cv::waitKey(1);

		if (key == 113) {	//"q"入力でbreak
			break;
		}

		else if (key == 115) {		////"s"入力で判定
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














