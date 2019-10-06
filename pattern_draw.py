"""
    Draw a given Android Mobile Password Pattern as GIF.
"""

from PIL import Image, ImageDraw
from math import sqrt
im_width, im_height = 400, 400
dot_radius = 10
min_distance = 10
positions = {
    1: (100, 100),
    2: (200, 100),
    3: (300, 100),
    4: (100, 200),
    5: (200, 200),
    6: (300, 200),
    7: (100, 300),
    8: (200, 300),
    9: (300, 300),
}

def draw_pattern(pattern, out_file = 'pattern.gif'):
    img = Image.new('RGB', (im_width, im_height))
    drw = ImageDraw.Draw(img)
    # Drawing the DOTS
    for dot in positions:
        start = (positions[dot][0] - dot_radius, positions[dot][1] - dot_radius)
        end = (positions[dot][0] + dot_radius, positions[dot][1] + dot_radius)
        drw.ellipse(start + end, fill=(255, 255, 255))

    # Drawing the lines
    frames = []
    img_temp = img.copy()
    for dot1, dot2 in zip(pattern, pattern[1:]):
        distance = sqrt((positions[dot1][0] - positions[dot2][0])**2 + (positions[dot1][1] - positions[dot2][1])**2)
        num_intermediates = int(distance/min_distance)
        img_temp_start = img_temp.copy()
        for i in range(num_intermediates):
            drw_tmp = ImageDraw.Draw(img_temp)
            (dot1x, dot1y), (dot2x, dot2y) = positions[dot1], positions[dot2]
            start = (dot1x + (dot2x - dot1x) * i / num_intermediates, dot1y + (dot2y - dot1y) * i / num_intermediates)
            end = (dot1x + (dot2x - dot1x) * (i + 1) / num_intermediates, dot1y + (dot2y - dot1y) * (i + 1)/ num_intermediates)
            drw_tmp.line(start + end, fill=(255, 0, 0), width=2)
            frames.append(img_temp)
            img_temp = img_temp.copy()
        img_temp = img_temp_start
        drw_tmp = ImageDraw.Draw(img_temp)
        drw_tmp.line(positions[dot1] + positions[dot2], fill=(255, 255, 255), width=2)
        frames.append(img_temp)

    img.save(out_file, save_all=True, append_images=frames, optimize=True, duration=40, loop=0)
    print(f'Pattern saved in {out_file}.')

if __name__ == '__main__':
    pattern_1 = [1, 6, 7, 8, 3, 2, 9, 5, 4]
    draw_pattern(pattern_1)