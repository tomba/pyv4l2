#version 300 es

precision mediump float;
precision mediump sampler2D;
precision mediump int;

in vec2 vTexCoord;
flat in int vTileIndex;

uniform float blackLevel;
uniform vec3 whiteBalance;
uniform sampler2D textures[6];
const float whiteLevel = 1.0;

out vec4 fragColor;

// Helper function to fetch and apply black level subtraction
float fetchPixel(sampler2D tex, ivec2 pos) {
    float rawValue = texelFetch(tex, pos, 0).r;
    // Subtract black level and normalize to [0,1] range
    return max(0.0, (rawValue - blackLevel) / (whiteLevel - blackLevel));
}

vec4 demosaic(sampler2D tex, ivec2 pixel) {
    int x = pixel.x % 2;
    int y = pixel.y % 2;

    float r = 0.0, g = 0.0, b = 0.0;

    if (y == 0) {
        if (x == 0) {
            // Red pixel
            r = fetchPixel(tex, pixel) * whiteBalance.r;
            g = (fetchPixel(tex, pixel + ivec2(1, 0)) +
                 fetchPixel(tex, pixel + ivec2(0, 1))) * 0.5 * whiteBalance.g;
            b = fetchPixel(tex, pixel + ivec2(1, 1)) * whiteBalance.b;
        } else {
            // Green pixel (in red row)
            g = fetchPixel(tex, pixel) * whiteBalance.g;
            r = fetchPixel(tex, pixel - ivec2(1, 0)) * whiteBalance.r;
            b = fetchPixel(tex, pixel + ivec2(0, 1)) * whiteBalance.b;
        }
    } else {
        if (x == 0) {
            // Green pixel (in blue row)
            g = fetchPixel(tex, pixel) * whiteBalance.g;
            r = fetchPixel(tex, pixel - ivec2(0, 1)) * whiteBalance.r;
            b = fetchPixel(tex, pixel + ivec2(1, 0)) * whiteBalance.b;
        } else {
            // Blue pixel
            b = fetchPixel(tex, pixel) * whiteBalance.b;
            g = (fetchPixel(tex, pixel - ivec2(1, 0)) +
                 fetchPixel(tex, pixel - ivec2(0, 1))) * 0.5 * whiteBalance.g;
            r = fetchPixel(tex, pixel - ivec2(1, 1)) * whiteBalance.r;
        }
    }

    return vec4(r, g, b, 1.0);
}

void main() {
    ivec2 texSize;
    ivec2 pixel;

    vec2 flippedCoord = vec2(vTexCoord.x, 1.0 - vTexCoord.y);

    switch(vTileIndex) {
        case 0:
            texSize = textureSize(textures[0], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[0], pixel);
            break;
        case 1:
            texSize = textureSize(textures[1], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[1], pixel);
            break;
        case 2:
            texSize = textureSize(textures[2], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[2], pixel);
            break;
        case 3:
            texSize = textureSize(textures[3], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[3], pixel);
            break;
        case 4:
            texSize = textureSize(textures[4], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[4], pixel);
            break;
        case 5:
            texSize = textureSize(textures[5], 0);
            pixel = ivec2(flippedCoord * vec2(texSize));
            fragColor = demosaic(textures[5], pixel);
            break;
        default:
            fragColor = vec4(1.0, 0.0, 0.0, 1.0); // Error color (red)
            break;
    }
}
