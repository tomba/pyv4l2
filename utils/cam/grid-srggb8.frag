#version 300 es

precision mediump float;
precision mediump sampler2D;
precision mediump int;

in vec2 vTexCoord;
flat in int vTileIndex;

uniform sampler2D textures[6];

out vec4 fragColor;

vec4 demosaic(sampler2D tex, ivec2 pixel) {
    int x = pixel.x % 2;
    int y = pixel.y % 2;

    float r = 0.0, g = 0.0, b = 0.0;

    if (y == 0) {
        if (x == 0) {
            // Red pixel
            r = texelFetch(tex, pixel, 0).r;
            g = (texelFetch(tex, pixel + ivec2(1, 0), 0).r +
                texelFetch(tex, pixel + ivec2(0, 1), 0).r) * 0.5;
            b = texelFetch(tex, pixel + ivec2(1, 1), 0).r;
        } else {
            // Green pixel (in red row)
            g = texelFetch(tex, pixel, 0).r;
            r = texelFetch(tex, pixel - ivec2(1, 0), 0).r;
            b = texelFetch(tex, pixel + ivec2(0, 1), 0).r;
        }
    } else {
        if (x == 0) {
            // Green pixel (in blue row)
            g = texelFetch(tex, pixel, 0).r;
            r = texelFetch(tex, pixel - ivec2(0, 1), 0).r;
            b = texelFetch(tex, pixel + ivec2(1, 0), 0).r;
        } else {
            // Blue pixel
            b = texelFetch(tex, pixel, 0).r;
            g = (texelFetch(tex, pixel - ivec2(1, 0), 0).r +
                texelFetch(tex, pixel - ivec2(0, 1), 0).r) * 0.5;
            r = texelFetch(tex, pixel - ivec2(1, 1), 0).r;
        }
    }

    return vec4(r, g, b, 1.0);
}

void main() {
    ivec2 texSize;
    ivec2 pixel;

    switch(vTileIndex) {
        case 0:
            texSize = textureSize(textures[0], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[0], pixel);
            break;
        case 1:
            texSize = textureSize(textures[1], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[1], pixel);
            break;
        case 2:
            texSize = textureSize(textures[2], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[2], pixel);
            break;
        case 3:
            texSize = textureSize(textures[3], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[3], pixel);
            break;
        case 4:
            texSize = textureSize(textures[4], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[4], pixel);
            break;
        case 5:
            texSize = textureSize(textures[5], 0);
            pixel = ivec2(vTexCoord * vec2(texSize));
            fragColor = demosaic(textures[5], pixel);
            break;
        default:
            fragColor = vec4(1.0, 0.0, 0.0, 1.0); // Error color (red)
            break;
    }
}
