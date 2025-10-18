% Assignment_187.m
% Main program to test all custom image processing functions

clear; clc; close all;

% ---- Step 1: Read your face image ----                                    
Icolor = imread('Img1.jpg'); % reading is allowed
figure; imshow(Icolor); title('Step 1: Original Color Image');

% ---- Step 2: Convert to grayscale (manual) ----
Igray = convertToGray_custom(Icolor);
figure;
subplot(1,2,1); imshow(Icolor); title('Original Color');
subplot(1,2,2); imshow(Igray); title('Step 2: Manual Grayscale Conversion');

% ---- Step 3: Invert grayscale image ----
Iinv = invertImage_custom(Igray);
figure;
subplot(1,2,1); imshow(Igray); title('Grayscale Image');
subplot(1,2,2); imshow(Iinv); title('Step 3: Inverted (Negative) Image');

% ---- Step 4: Read second image ----
I2 = imread('Img2.jpg');
if size(I2, 3) == 3
    I2 = convertToGray_custom(I2); % convert only if color
end

% Resize manually if sizes differ (simple crop method)
[r1, c1] = size(Igray);
[r2, c2] = size(I2);
if r1 ~= r2 || c1 ~= c2
    I2 = I2(1:min(r1,r2), 1:min(c1,c2)); % crop to match
    Igray = Igray(1:min(r1,r2), 1:min(c1,c2));
end

% ---- Step 5: Add and Subtract images ----
[Iadd, Isub] = addSubtract_custom(Igray, I2);
figure;
subplot(1,3,1); imshow(Igray); title('Original Grayscale');
subplot(1,3,2); imshow(Iadd); title('Step 5: Image Addition');
subplot(1,3,3); imshow(Isub); title('Step 5: Image Subtraction');

% ---- Step 6: Contrast Adjustment ----
Ics = contrastStretch_custom(Igray);
figure;
subplot(1,2,1); imshow(Igray); title('Original Grayscale');
subplot(1,2,2); imshow(Ics); title('Step 6: Contrast Adjusted Image');
