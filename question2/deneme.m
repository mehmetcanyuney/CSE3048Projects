function r = mi(x,y,p,q,test)
  temp = 0;
  for r=1:p
    for s=1:q
        temp = temp + double(test(x+r,y+s));
    end
  end
  r = temp/p/q;
end

function t = mt(p,q,i)
  temp = 0;
  for r=1:p
    for s=1:q
        temp = temp + double(i(r,s));
    end
  end
  t = temp/p/q;
end


function r = a(x,y,p,q,test,i,MT,lower1)
 temp = 0;
  for r=1:p
    for s=1:q
        temp = temp + (double(i(r,s))-MT)*(double(test(x+r,y+s))-mi(x,y,p,q,test));
    end
  end
  upper = temp
  
  temp = 0;
  for r=1:p
    for s=1:q
        temp = temp + ((double(test(x+r,y+s))-mi(x,y,p,q,test))^2);
    end
  end
  lower2 = sqrt(temp);

  r= upper/lower1/lower2;
end


%reads images and converts gray
i1 = imread('train1.png');
i1 = rgb2gray(i1);
i1 = imresize(i1, [87 120]);
%imshow(i1)

i2 = imread('train2.png');
i2 = rgb2gray(i2);
i2 = imresize(i2, [87 120]);
%imshow(i2)

i3 = imread('train3.png');
i3 = rgb2gray(i3);
i3 = imresize(i3, [87 120]);
%imshow(i3)

i4 = imread('train4.png');
i4 = rgb2gray(i4);
i4 = imresize(i4, [87 120]);
%imshow(i4)

test = imread('test.jpg');
test = rgb2gray(test);
%imshow(test)

i5 = (i2 + i4)./2;

[m,n] = size(test);
[p,q] = size(i1);
x = [];
MT = mt(p,q,i5);

temp = 0;
for r=1:p
    for s=1:q
        temp = temp + ((double(i5(r,s))-MT)^2);
    end
end
lower1 = sqrt(temp);

for k = 1:400:(m-p)
    for l = 1:200:(n-q)
        l,k
        x = [x; [k,l,a(k,l,p,q,test,i5,MT,lower1)]];
    end
end
%sort the similarities
final = sortrows(x,3);
fx = final(end,1);
fy = final(end,2);

%draw a rectangle
test(fx, fy:fy+87) = zeros(1, 88);
test(fx+120, fy:fy+87) = zeros(1, 88);
test(fx:fx+120, fy) = zeros(1, 121);
test(fx:fx+120, fy+87) = zeros(1, 121);