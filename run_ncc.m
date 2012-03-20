function run_ncc(im_filename)

    if nargin < 1,  % no filename provided
        im_filename = 'lena.png';
    end

    % Load image, get size, extract red channel
    im = imread(im_filename);
    [h, w, ~] = size(im);
    im_red = im(:,:,1);

    % Note these limits are different from python as
    % matlab uses 1-based indexing, and also uses inclusive
    % indices for the end, unlike python
    hrng = (round(h/4)+1):(round(3 * h / 4));
    wrng = (round(w/4)+1):(round(3 * w / 4));
    im_centre_red = im_red(hrng, wrng);

    fprintf('image size is %dx%d\n', size(im_red));
    fprintf('template size is %dx%d\n', size(im_centre_red));
    fprintf('template min/max = %f/%f\n', min(im_centre_red(:)), max(im_centre_red(:)));
    fprintf('template mean = %f\n', mean(im_centre_red(:)));

    % There are no configuration options for normxcorr2
    ncc_result = normxcorr2(im_centre_red, im_red);

    figure();
    imagesc(ncc_result);
    title(sprintf('ncc result, size %dx%d', size(ncc_result)));
    imwrite(ncc_result, 'matlab_result.png');

    % Save outputs
    save('matlab_ncc_workspace','im_red', 'im_centre_red', 'ncc_result');

