function Ics = contrastStretch_custom(I)
% contrastStretch_custom: manually increases contrast of a grayscale image
% Formula: Ics = (I - min) * (255 / (max - min))

I = double(I);
minVal = min(I(:));
maxVal = max(I(:));

Ics = (I - minVal) * (255 / (maxVal - minVal));
Ics = uint8(Ics);
end
