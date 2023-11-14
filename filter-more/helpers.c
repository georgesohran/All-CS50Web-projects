#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int value = round(((float)image[i][j].rgbtBlue + (float)image[i][j].rgbtRed + (float)image[i][j].rgbtGreen)/3);
            image[i][j].rgbtBlue = value;
            image[i][j].rgbtRed = value;
            image[i][j].rgbtGreen = value;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width/2; i++)
    {
        for (int j = 0; j < height; j++)
        {
            RGBTRIPLE temp = image[j][i];

            image[j][i].rgbtBlue = image[j][width-i-1].rgbtBlue;
            image[j][i].rgbtRed = image[j][width-i-1].rgbtRed;
            image[j][i].rgbtGreen = image[j][width-i-1].rgbtGreen;

            image[j][width-i-1].rgbtBlue = temp.rgbtBlue;
            image[j][width-i-1].rgbtRed = temp.rgbtRed;
            image[j][width-i-1].rgbtGreen = temp.rgbtGreen;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_red = 0;
            int sum_blue = 0;
            int sum_green = 0;

            int count = 0;

            for (int y = -1; y < 2; y++)
            {
                for (int x = -1; x < 2; x++)
                {
                    if (i + x >= 0 && i + x < width && j + y >= 0 && j + y < height)
                    {
                        sum_red += image[i + x][j + y].rgbtRed;
                        sum_blue += image[i + x][j + y].rgbtBlue;
                        sum_green += image[i + x][j + y].rgbtGreen;

                        count++;
                    }
                }
            }
            temp[i][j].rgbtRed = round((float) sum_red / (float) count);
            temp[i][j].rgbtBlue = round((float) sum_blue / (float) count);
            temp[i][j].rgbtGreen = round((float) sum_green / (float) count);
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}

int Gx[3][3] = {{-1,0,1},
              {-2,0,2},
              {-1,0,1}};

int Gy[3][3] = {{-1,-2,-1},
              {0,0,0},
              {-1,-2,-1}};

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gx_red = 0;
            int gx_blue = 0;
            int gx_green = 0;

            int gy_red = 0;
            int gy_blue = 0;
            int gy_green = 0;

            for (int y = -1; y < 2; y++)
            {
                for (int x = -1; x < 2; x++)
                {
                    int indx_x = x + 1
                    int indx_y = y + 1

                    int sum_red = 0;
                    int sum_blue = 0;
                    int sum_green = 0;

                    if (i + x >= 0 && i + x < width && j + y >= 0 && j + y < height)
                    {

                    }
                }
            }
        }
    }
    return;
}
