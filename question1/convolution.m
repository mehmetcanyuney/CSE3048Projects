function [conv_result] = convolution(image, kernel, padding)
    [kernel_rowsize, kernel_colsize] = size(kernel);
    
    [image_rowsize, image_colsize] = size(image);
    
    for row=1:image_rowsize
      for col=1:image_colsize
        conv_sum = 0;
        for inner_row=1:kernel_rowsize
          for inner_col=1:kernel_colsize
            loc_col = col + (inner_col - 2);
            loc_row = row + (inner_row - 2);
            
            if ((loc_col >= 1) && (loc_col <= image_colsize) && (loc_row >= 1) && (loc_row <= image_rowsize))
              conv_sum = conv_sum + (image(loc_row, loc_col) * kernel(inner_row, inner_col));
            endif
            if (padding == 1)
              if (loc_col < 1)
                if (loc_row < 1)
                  conv_sum = conv_sum + (image(1,1) * kernel(inner_row, inner_col));
                elseif (loc_row > image_rowsize)
                  conv_sum = conv_sum + (image(image_rowsize,1) * kernel(inner_row, inner_col));
                else
                  conv_sum = conv_sum + (image(loc_row,1) * kernel(inner_row, inner_col));
                endif
              elseif ((loc_col >= 1) && (loc_col <= image_colsize))
                if (loc_row < 1)
                  conv_sum = conv_sum + (image(1,loc_col) * kernel(inner_row, inner_col));
                elseif (loc_row > image_rowsize)
                  conv_sum = conv_sum + (image(image_rowsize,loc_col) * kernel(inner_row, inner_col));
                endif
              elseif (loc_col > image_colsize)
                if (loc_row < 1)
                  conv_sum = conv_sum + (image(1,image_colsize) * kernel(inner_row, inner_col));
                elseif (loc_row > image_rowsize)
                  conv_sum = conv_sum + (image(image_rowsize,image_colsize) * kernel(inner_row, inner_col));
                else
                  conv_sum = conv_sum + (image(loc_row,image_colsize) * kernel(inner_row, inner_col));
                endif
              endif
            endif
          endfor
        endfor
        
        row,col
        
        if (conv_sum < 0)
          conv_sum = 0;
        elseif (conv_sum > 256)
          conv_sum = 256;
        endif
        
        conv_result(row, col) = conv_sum;
      endfor
    endfor
endfunction
