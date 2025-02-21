#version 300 es
precision highp float;

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 texCoordAndTile;  // xy = texture coords, z = tile index

out vec2 vTexCoord;
flat out int vTileIndex;

void main() {
	gl_Position = vec4(position, 1.0);
	vTexCoord = texCoordAndTile.xy;
	vTileIndex = int(texCoordAndTile.z);
}
