function Iinv = invertImage_custom(I)
% invertImage_custom: manually inverts (negates) a grayscale image
% Formula: Iinv = 255 - I

Iinv = 255 - double(I);
Iinv = uint8(Iinv);
end
