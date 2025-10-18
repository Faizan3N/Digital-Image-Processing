function G = convertToGray_custom(I)
% convertToGray_custom: manually converts RGB image to grayscale
% Formula: G = 0.299*R + 0.587*G + 0.114*B

R = I(:,:,1);
Gg = I(:,:,2);
B = I(:,:,3);

G = 0.299*double(R) + 0.587*double(Gg) + 0.114*double(B);
G = uint8(G);
end
