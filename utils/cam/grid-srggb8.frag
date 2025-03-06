#version 310 es

#extension GL_OES_EGL_image_external : enable
#extension GL_OES_EGL_image_external_essl3 : enable

precision mediump float;
precision mediump sampler2D;
precision mediump int;

in vec2 vTexCoord;
flat in int vTileIndex;

uniform float blackLevel;
uniform float whiteLevel;
uniform vec3 whiteBalance;
uniform float gamma;
uniform mat3 colorCorrectionMatrix;
uniform samplerExternalOES textures[6];

out vec4 fragColor;

// Helper function to fetch and apply black level subtraction
float fetchPixel(samplerExternalOES tex, ivec2 pos) {
    float rawValue = texelFetch(tex, pos, 0).r;

    // Black level adjustment
    rawValue = max(0.0, rawValue - blackLevel);

    // White level adjustment
    rawValue = rawValue / (whiteLevel - blackLevel);

    return rawValue;
}

vec4 demosaic(samplerExternalOES tex, ivec2 pixel) {
    int x = pixel.x % 2;
    int y = pixel.y % 2;

    float r, g, b;

    if (y == 0) {
        if (x == 0) {
            // Red pixel
            r = fetchPixel(tex, pixel);
            g = (fetchPixel(tex, pixel + ivec2(1, 0)) + fetchPixel(tex, pixel + ivec2(0, 1))) * 0.5;
            b = fetchPixel(tex, pixel + ivec2(1, 1));
        } else {
            // Green pixel (in red row)
            g = fetchPixel(tex, pixel);
            r = fetchPixel(tex, pixel - ivec2(1, 0));
            b = fetchPixel(tex, pixel + ivec2(0, 1));
        }
    } else {
        if (x == 0) {
            // Green pixel (in blue row)
            g = fetchPixel(tex, pixel);
            r = fetchPixel(tex, pixel - ivec2(0, 1));
            b = fetchPixel(tex, pixel + ivec2(1, 0));
        } else {
            // Blue pixel
            b = fetchPixel(tex, pixel);
            g = (fetchPixel(tex, pixel - ivec2(1, 0)) + fetchPixel(tex, pixel - ivec2(0, 1))) * 0.5;
            r = fetchPixel(tex, pixel - ivec2(1, 1));
        }
    }

    vec3 c = vec3(r, g, b);

    c *= whiteBalance;
    c = clamp(c, 0.0, 1.0);

    c *= colorCorrectionMatrix;
    c = clamp(c, 0.0, 1.0);

    c = pow(c, vec3(1.0/gamma));

    return vec4(c, 1.0);
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
