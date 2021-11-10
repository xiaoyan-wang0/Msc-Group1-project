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

 Date: 10/11/2021 16:36:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for reviews
-- ----------------------------
DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews`  (
  `reviewId` int(0) NOT NULL AUTO_INCREMENT,
  `movieId` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `content` json NULL,
  `type` int(0) NULL DEFAULT NULL COMMENT '1: tmdb ;  2: Imdb; 3: youtubu; 4: Twitter',
  `createTime` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`reviewId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 40 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of reviews
-- ----------------------------

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
  `movieId` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `toxic` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sentiment` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usercomments
-- ----------------------------

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo`  (
  `userInfoId` int(0) NOT NULL AUTO_INCREMENT,
  `userId` int(0) NOT NULL,
  `image` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `birthday` datetime(0) NULL DEFAULT NULL,
  `likeNum` int(0) NULL DEFAULT NULL,
  `followNum` int(0) NULL DEFAULT NULL,
  `age` int(0) NULL DEFAULT NULL,
  `overView` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `movieTags` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`userInfoId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of userinfo
-- ----------------------------

-- ----------------------------
-- Table structure for usermovies
-- ----------------------------
DROP TABLE IF EXISTS `usermovies`;
CREATE TABLE `usermovies`  (
  `Id` int(0) NOT NULL AUTO_INCREMENT,
  `userId` int(0) NOT NULL,
  `movieId` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `type` int(0) NOT NULL COMMENT 'type = 1 means movie user like\r\ntype = 2 means movie user hate',
  `createTime` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usermovies
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
