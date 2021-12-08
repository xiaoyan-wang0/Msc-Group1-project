module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  transform: {
    '^.+\\.vue$': 'vue-jest',
  },
  "collectCoverage": true,
  "collectCoverageFrom": ["**/*.{js,vue}"],
  setupFiles: [
    './tests/unit/setup.js'	// setup.js 启动文件的路径
]
}
