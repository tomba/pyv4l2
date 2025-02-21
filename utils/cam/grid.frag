#version 310 es

precision mediump float;
precision mediump sampler2D;

in vec2 vTexCoord;
flat in int vTileIndex;

uniform samplerExternalOES textures[6];  // Array of textures for each tile

out vec4 fragColor;

void main() {
    // Select texture based on tile index
    vec4 texColor;
    if (vTileIndex == 0) texColor = texture(textures[0], vTexCoord);
    else if (vTileIndex == 1) texColor = texture(textures[1], vTexCoord);
    else if (vTileIndex == 2) texColor = texture(textures[2], vTexCoord);
    else if (vTileIndex == 3) texColor = texture(textures[3], vTexCoord);
    else if (vTileIndex == 4) texColor = texture(textures[4], vTexCoord);
    else texColor = texture(textures[5], vTexCoord);

    fragColor = texColor;
}
