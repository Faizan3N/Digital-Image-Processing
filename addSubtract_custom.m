function [Iadd, Isub] = addSubtract_custom(I1, I2)
% addSubtract_custom: manually performs image addition and subtraction
% Ensures output stays within [0,255]

I1 = double(I1);
I2 = double(I2);

Iadd = I1 + I2;
Isub = I1 - I2;

% Clip values to 0–255 range
Iadd(Iadd > 255) = 255;
Iadd(Iadd < 0) = 0;
Isub(Isub > 255) = 255;
Isub(Isub < 0) = 0;

Iadd = uint8(Iadd);
Isub = uint8(Isub);
end
