/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : movie

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 17/10/2021 18:46:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `userId` int(0) NOT NULL AUTO_INCREMENT,
  `userName` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `email` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `createTime` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`userId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (4, '+', '12345', 'dafd3b5a5240ff245e8249d9137525a2', '2021-10-11 17:40:54');
INSERT INTO `user` VALUES (5, 'ethanzhang', 'ethan@gmail.com', 'dafd3b5a5240ff245e8249d9137525a2', '2021-10-12 12:05:44');

-- ----------------------------
-- Table structure for usercomments
-- ----------------------------
DROP TABLE IF EXISTS `usercomments`;
CREATE TABLE `usercomments`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `userId` int(0) NULL DEFAULT NULL,
  `tagId` int(0) NULL DEFAULT NULL,
  `comment` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `createTime` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `movieId` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usercomments
-- ----------------------------
INSERT INTO `usercomments` VALUES (1, 5, NULL, 'hello', '2021-10-15 08:16:36', 1);
INSERT INTO `usercomments` VALUES (2, 5, NULL, 'hey', '2021-10-15 08:17:33', 1);
INSERT INTO `usercomments` VALUES (3, 5, NULL, '12', '2021-10-15 08:18:49', 1);
INSERT INTO `usercomments` VALUES (5, 5, NULL, 'good actor', '2021-10-15 08:38:11', 1);

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo`  (
  `userInfoId` int(0) NOT NULL AUTO_INCREMENT,
  `userId` int(0) NOT NULL,
  `image` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pm` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `likeNum` int(0) NULL DEFAULT NULL,
  `followNum` int(0) NULL DEFAULT NULL,
  `age` int(0) NULL DEFAULT NULL,
  `constellation` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `movieTags` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`userInfoId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES (1, 1, '', 'qqq', 1, 12, 24, 'wtf', 'active,fight');

-- ----------------------------
-- Table structure for usermovies
-- ----------------------------
DROP TABLE IF EXISTS `usermovies`;
CREATE TABLE `usermovies`  (
  `Id` int(0) NOT NULL AUTO_INCREMENT,
  `userId` int(0) NOT NULL,
  `moiveId` int(0) NULL DEFAULT NULL,
  `type` int(0) NULL DEFAULT NULL,
  `createTime` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usermovies
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
