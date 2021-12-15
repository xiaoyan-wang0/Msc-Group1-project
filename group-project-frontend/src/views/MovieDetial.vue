 <template>
  <section class="amdb-details spad">
    <div class="">
      <a-modal
        :visible="isShowTrailer && video_id.length > 0"
        :maskClosable="true"
        :closable="false"
        :footer="null"
        :destroyOnClose="true"
        :width="trailerWidth"
        @cancel="handleCancel"
      >
        <YoutubeVue3
          ref="youtube"
          :videoid="video_id"
          :width="trailerWidth"
          :autoplay="0"
          :height="400"
        />
      </a-modal>
      <el-dialog
        v-model="addCommentsDialog"
        title="Warning"
        width="30%"
        center
        v-loading="commentConfirmLoading"
      >
        <span> Are you sure to publich your comment?</span>
        <br />
        <br />
        <span style="font-weight: 600">{{ popToxicText }}</span>
        <br />
        <span style="font-weight: 600">{{ popSentimentText }}</span>
        <br />
        <br />
        <span style="font-weight: 600">{{ popHightToxicText }}</span>
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="addCommentsDialog = false">Cancel</el-button>
            <el-button type="primary" @click="confirmAddComment"
              >Confirm</el-button
            >
          </span>
        </template>
      </el-dialog>

      <el-dialog
        v-model="reportCommentsDialog"
        title="Warning"
        width="30%"
        center
        v-loading="commentConfirmLoading"
      >
        <span style="font-weight: 600">
          Are you sure to report this comment?</span
        >
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="reportCommentsDialog = false">Cancel</el-button>
            <el-button type="primary" @click="confirmReportComment"
              >Confirm</el-button
            >
          </span>
        </template>
      </el-dialog>
    </div>
    <div class="container">
      <div class="amdb__details__content">
        <div class="row">
          <div class="col-lg-3">
            <div class="amdb__details__pic set-bg">
              <img
                :src="moviePoster + movie.poster_path"
                alt="Movie Poster"
                class="amdb__details__pic set-bg"
                @click="ShowTrailer()"
              />
            </div>
          </div>
          <div class="col-lg-9">
            <div class="amdb__details__text">
              <div class="amdb__details__title">
                <h3>{{ movie.original_title }}</h3>
                <span>{{ movie.release_date }}</span>
              </div>
              <div class="amdb__details__rating">
                <div class="rating">
                  <a-rate v-model:value="start" disabled allowHalf />
                  <p>{{ movie.vote_average }}</p>
                </div>
              </div>

              <p style="font-size: 20px">{{ movie.overview }}</p>

              <div class="amdb__details__widget">
                <div class="row">
                  <div class="col-lg-6 col-md-6">
                    <ul>
                      <li><span>Type:</span> Movie</li>
                      <li><span>Adult:</span> {{ movie.adult }}</li>
                      <li>
                        <span>Genres:</span>
                        <span
                          v-for="item in movie.genres"
                          :key="item.id"
                          style="width: fit-content; margin-right: 10px"
                          >{{ item.name }}</span
                        >
                      </li>
                    </ul>
                  </div>
                  <div class="col-lg-6 col-md-6">
                    <ul>
                      <li><span>vote count:</span>{{ movie.vote_count }}</li>
                      <li><span>Popularity:</span> {{ movie.popularity }}</li>
                      <li>
                        <span>Homepage</span
                        ><a :href="movie.homepage" target="_blank">
                          {{ movie.homepage }}</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>

                <div class="movie-tag-group">
                  <div class="morebutton"></div>
                  <div class="movie-casts">
                    <a-avatar
                      :size="{
                        xs: 24,
                        sm: 32,
                        md: 40,
                        lg: 64,
                        xl: 80,
                        xxl: 100,
                      }"
                      v-for="item in castList"
                      :key="item.id"
                      class="pichover"
                      @click="showCastDetail(item.id)"
                      style="margin: 5px"
                    >
                      <template #icon>
                        <img
                          :src="
                            item.profile_path != null
                              ? moviePoster + item.profile_path
                              : emptyprofile
                          "
                          alt="Cast profile"
                        />
                      </template>
                    </a-avatar>
                  </div>
                  <el-dialog v-model="isShowCastDetail" title="Detail">
                    <el-descriptions class="margin-top" :column="1">
                      <el-descriptions-item label="Name:">{{
                        castDetail.name
                      }}</el-descriptions-item>
                      <el-descriptions-item label="Birthday:">{{
                        castDetail.birthday
                      }}</el-descriptions-item>
                      <el-descriptions-item label="Department:">
                        <el-tag size="small">{{
                          castDetail.known_for_department
                        }}</el-tag>
                      </el-descriptions-item>
                      <el-descriptions-item label="Popularity:">{{
                        castDetail.popularity
                      }}</el-descriptions-item>
                      <el-descriptions-item label="Also known as:">{{
                        castDetail.also_known_as
                      }}</el-descriptions-item>
                      <el-descriptions-item label="Biography:">{{
                        castDetail.biography
                      }}</el-descriptions-item>
                    </el-descriptions>
                    <template #footer>
                      <span class="dialog-footer">
                        <el-button
                          type="primary"
                          @click="isShowCastDetail = false"
                        >
                          Close
                        </el-button>
                      </span>
                    </template>
                  </el-dialog>
                </div>
              </div>
              <div class="amdb__details__btn">
                <a @click="addLikeList()" class="follow-btn">
                  <i class="fa fa-heart"></i> ADD Like list
                </a>
                <a @click="ShowTrailer()" class="follow-btn"
                  ><i class="fa fa-play"></i> <span>Watch trailer</span>
                </a>
                <a class="follow-btn fb_share_btn"
                  ><i class="fab fa-facebook"></i>
                  <span> Facebook Share</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="amdb__details__review">
            <div class="section-title">
              <h5>reviews</h5>
            </div>
            <a-tabs
              v-loading="commentLoading"
              @change="changeCommentTab(activeKey)"
              v-model:activeKey="activeKey"
              :tabBarStyle="{ color: 'white' }"
            >
              <a-tab-pane key="amdb" tab="AMDB reviews" style="">
                <div class="comment-div-amdb">
                  <div class="section-title">
                    <div class="comment-filter">
                      <div class="comment-title">
                        <h5>AMDB Comment</h5>
                      </div>
                      <div class="filter-select">
                        <a-select
                          placeholder="Filter"
                          style="width: 150px"
                          @change="handleFilterChange"
                        >
                          <a-select-option value="all">All</a-select-option>
                          <a-select-opt-group>
                            <template #label>
                              <span> Toxic Degree </span>
                            </template>
                            <a-select-option value="notoxic"
                              >Non Toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
                            >
                            <a-select-option value="neutral"
                              >Neutral</a-select-option
                            >
                            <a-select-option value="negative"
                              >Negative</a-select-option
                            >
                          </a-select-opt-group>
                        </a-select>
                      </div>
                    </div>
                  </div>
                  <el-scrollbar max-height="500px">
                    <a-empty v-if="amdbreview.length < 1">
                      <template #description>
                        <span>
                          <!-- Customize -->
                          <a>Sorry, don't have now</a>
                        </span>
                      </template>
                    </a-empty>
                    <div
                      class="comment-wrap"
                      v-for="item in amdbreview"
                      :key="item.id"
                    >
                      <div class="amdb__review__item">
                        <div class="amdb__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar
                                :src="
                                  currentUser
                                    ? AMDBAPI +
                                      'member/getUserImage?userId=' +
                                      item.userId
                                    : emptyprofile
                                "
                              />
                            </div>
                          </div>
                        </div>
                        <div class="amdb__review__item__text">
                          <h6 class="comment-author">
                            {{ item.userName }}
                          </h6>
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="judgeBadWordOther(item.comment)"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">
                              {{ formatDate(item.createTime) }}
                            </div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{
                                  "Toxicity rate: " +
                                  changeToPercent(item.toxic) +
                                  showToxicText(item.toxic)
                                }}
                                <a-popover title="Toxicity">
                                  <template #content>
                                    <p>
                                      Green Skull:
                                      <br />
                                      0-53 Percent of Toxicity Chance - Most
                                      likely Non-Toxic
                                    </p>
                                    <p>
                                      Red Skull:
                                      <br />
                                      Above 54 Percent of Toxicity Chance -
                                      Almost Certainly Toxic
                                    </p>
                                  </template>
                                  <img
                                    :src="showToxicImg(item.toxic)"
                                    style="height: 30px"
                                    alt=""
                                  />
                                </a-popover>
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentimentText(item.sentiment) }}
                                <a-popover title="Sentimental">
                                  <template #content>
                                    <p>
                                      Green Similing Face:
                                      <br />
                                      Most Likely Positive
                                    </p>
                                    <p>
                                      Yellow Normal Face:
                                      <br />
                                      Most Likely Neutral
                                    </p>
                                    <p>
                                      Red Sad Face:
                                      <br />
                                      Most Likely Negative
                                    </p>
                                  </template>
                                  <img
                                    :src="showSentimentImg(item.sentiment)"
                                    style="height: 30px; margin-left: 5px"
                                    alt=""
                                  />
                                </a-popover>
                              </li>
                              <li class="report">
                                <a @click="amdbReport(item)">Report</a>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </el-scrollbar>
                  <div class="amdb__details__form">
                    <a-comment>
                      <template #avatar>
                        <a-avatar
                          :src="
                            currentUser
                              ? AMDBAPI +
                                'member/getUserImage?userId=' +
                                currentUser.data.userId
                              : emptyprofile
                          "
                          alt="Avatar"
                        />
                      </template>
                      <template #content>
                        <a-form-item>
                          <a-textarea
                            v-model:value="commentsValue"
                            :rows="4"
                            :maxlength="5000"
                            show-count
                          />
                        </a-form-item>
                        <a-form-item>
                          <button
                            class="site-btn"
                            html-type="submit"
                            :loading="submitting"
                            @click="handleSubmit()"
                            :disabled="commentConfirmLoading"
                          >
                            Add Comment
                          </button>
                        </a-form-item>
                      </template>
                    </a-comment>
                  </div>
                </div>
              </a-tab-pane>

              <a-tab-pane key="tmdb" tab="TMDB reviews" v-if="tmdbreview">
                <div class="comment-div">
                  <div class="section-title">
                    <div class="comment-filter">
                      <h5>TMDB Comment</h5>
                      <div class="filter-select">
                        <a-select
                          placeholder="Filter"
                          style="width: 150px"
                          @change="handleTMDBFilterChange"
                        >
                          <a-select-option value="all">All</a-select-option>
                          <a-select-opt-group>
                            <template #label>
                              <span> Toxic Degree </span>
                            </template>
                            <a-select-option value="notoxic"
                              >Non Toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
                            >
                            <a-select-option value="neutral"
                              >Neutral</a-select-option
                            >
                            <a-select-option value="negative"
                              >Negative</a-select-option
                            >
                          </a-select-opt-group>
                        </a-select>
                      </div>
                    </div>
                  </div>
                  <el-scrollbar max-height="700px">
                    <a-empty v-if="tmdbreview.length < 1">
                      <template #description>
                        <span>
                          <!-- Customize -->
                          <a>Sorry, don't have now</a>
                        </span>
                      </template>
                    </a-empty>
                    <div
                      class="comment-wrap"
                      v-for="item in tmdbreview"
                      :key="item.id"
                    >
                      <div class="amdb__review__item">
                        <div class="amdb__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar
                                :src="
                                  item.author_details.avatar_path
                                    ? linkCheck(item.author_details.avatar_path)
                                      ? checkLink(
                                          item.author_details.avatar_path
                                        )
                                      : moviePoster +
                                        item.author_details.avatar_path
                                    : emptyprofile
                                "
                              />
                            </div>
                          </div>
                        </div>
                        <div class="amdb__review__item__text">
                          <h6 class="comment-author">{{ item.author }}</h6>
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="judgeBadWordOther(item.content)"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">
                              {{ formatDate(item.created_at) }}
                            </div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{
                                  "Toxicity rate: " +
                                  changeToPercent(item.toxic) +
                                  showToxicText(item.toxic[0])
                                }}
                                <a-popover title="Toxicity">
                                  <template #content>
                                    <p>
                                      Green Skull:
                                      <br />
                                      0-53 Percent of Toxicity Chance - Most
                                      likely Non-Toxic
                                    </p>
                                    <p>
                                      Red Skull:
                                      <br />
                                      Above 54 Percent of Toxicity Chance -
                                      Almost Certainly Toxic
                                    </p>
                                  </template>
                                  <img
                                    :src="showToxicImg(item.toxic)"
                                    style="height: 30px"
                                    alt=""
                                  />
                                </a-popover>
                              </li>
                              <li class="report">
                                {{ showSentimentText(item.sentiment)
                                }}<a-popover title="Sentimental">
                                  <template #content>
                                    <p>
                                      Green Similing Face:
                                      <br />
                                      Most Likely Positive
                                    </p>
                                    <p>
                                      Yellow Normal Face:
                                      <br />
                                      Most Likely Neutral
                                    </p>
                                    <p>
                                      Red Sad Face:
                                      <br />
                                      Most Likely Negative
                                    </p>
                                  </template>
                                  <img
                                    :src="showSentimentImg(item.sentiment)"
                                    style="height: 30px; margin-left: 5px"
                                    alt=""
                                /></a-popover>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </el-scrollbar>
                </div>
              </a-tab-pane>
              <a-tab-pane key="imdb" tab="IMDB reviews">
                <div class="comment-div">
                  <div class="section-title">
                    <div class="comment-filter">
                      <h5>IMDB Comment</h5>
                      <div class="filter-select">
                        <a-select
                          placeholder="Filter"
                          style="width: 150px"
                          @change="handleIMDBFilterChange"
                        >
                          <a-select-option value="all">All</a-select-option>
                          <a-select-opt-group>
                            <template #label>
                              <span> Toxic Degree </span>
                            </template>
                            <a-select-option value="notoxic"
                              >Non Toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
                            >
                            <a-select-option value="neutral"
                              >Neutral</a-select-option
                            >
                            <a-select-option value="negative"
                              >Negative</a-select-option
                            >
                          </a-select-opt-group>
                        </a-select>
                      </div>
                    </div>
                  </div>
                  <el-scrollbar max-height="700px">
                    <a-empty v-if="imdbreview.length < 1">
                      <template #description>
                        <span>
                          <!-- Customize -->
                          <a>Sorry, don't have now</a>
                        </span>
                      </template>
                    </a-empty>
                    <div
                      class="comment-wrap"
                      v-for="item in imdbreview"
                      :key="item.id"
                    >
                      <div class="amdb__review__item">
                        <div class="amdb__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="emptyprofile" />
                            </div>
                          </div>
                        </div>
                        <div class="amdb__review__item__text">
                          <h6 class="comment-author">{{ item.username }}</h6>
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="judgeBadWordOther(item.content)"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">{{ item.date }}</div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{
                                  "Toxicity rate: " +
                                  changeToPercent(item.toxic) +
                                  showToxicText(item.toxic[0])
                                }}<a-popover title="Toxicity">
                                  <template #content>
                                    <p>
                                      Green Skull:
                                      <br />
                                      0-53 Percent of Toxicity Chance - Most
                                      likely Non-Toxic
                                    </p>
                                    <p>
                                      Red Skull:
                                      <br />
                                      Above 54 Percent of Toxicity Chance -
                                      Almost Certainly Toxic
                                    </p>
                                  </template>
                                  <img
                                    :src="showToxicImg(item.toxic)"
                                    style="height: 30px"
                                    alt=""
                                /></a-popover>
                              </li>
                              <li
                                :class="
                                  item.warningSpoilers
                                    ? 'sentiemnt-rate'
                                    : 'report'
                                "
                              >
                                {{ showSentimentText(item.sentiment)
                                }}<a-popover title="Sentimental">
                                  <template #content>
                                    <p>
                                      Green Similing Face:
                                      <br />
                                      Most Likely Positive
                                    </p>
                                    <p>
                                      Yellow Normal Face:
                                      <br />
                                      Most Likely Neutral
                                    </p>
                                    <p>
                                      Red Sad Face:
                                      <br />
                                      Most Likely Negative
                                    </p>
                                  </template>
                                  <img
                                    :src="showSentimentImg(item.sentiment)"
                                    style="height: 30px; margin-left: 5px"
                                    alt=""
                                /></a-popover>
                              </li>
                              <li class="report" v-if="item.warningSpoilers">
                                {{
                                  item.warningSpoilers ? "Spoiler warning " : ""
                                }}
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </el-scrollbar>
                </div>
              </a-tab-pane>
              <a-tab-pane key="youtube" tab="Youtube reviews">
                <div class="comment-div">
                  <div class="section-title">
                    <div class="comment-filter">
                      <h5>Youtube Comment</h5>
                      <div class="filter-select">
                        <a-select
                          placeholder="Filter"
                          style="width: 150px"
                          @change="handleYoutubeFilterChange"
                        >
                          <a-select-option value="all">All</a-select-option>
                          <a-select-opt-group>
                            <template #label>
                              <span> Toxic Degree </span>
                            </template>
                            <a-select-option value="notoxic"
                              >Non Toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
                            >
                            <a-select-option value="neutral"
                              >Neutral</a-select-option
                            >
                            <a-select-option value="negative"
                              >Negative</a-select-option
                            >
                          </a-select-opt-group>
                        </a-select>
                      </div>
                    </div>
                  </div>
                  <el-scrollbar max-height="700px">
                    <a-empty v-if="youtubereview.length < 1">
                      <template #description>
                        <span>
                          <!-- Customize -->
                          <a>Sorry, don't have now</a>
                        </span>
                      </template>
                    </a-empty>
                    <div
                      class="comment-wrap"
                      v-for="item in youtubereview"
                      :key="item.id"
                    >
                      <div class="amdb__review__item">
                        <div class="amdb__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="item.profile_picture" />
                            </div>
                          </div>
                        </div>
                        <div class="amdb__review__item__text">
                          <h6 class="comment-author">{{ item.username }}</h6>
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="judgeBadWordOther(item.review)"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">
                              {{ formatDate(item.time) }}
                            </div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{
                                  "Toxicity rate: " +
                                  changeToPercent(item.toxic) +
                                  showToxicText(item.toxic[0])
                                }}<a-popover title="Toxicity">
                                  <template #content>
                                    <p>
                                      Green Skull:
                                      <br />
                                      0-53 Percent of Toxicity Chance - Most
                                      likely Non-Toxic
                                    </p>
                                    <p>
                                      Red Skull:
                                      <br />
                                      Above 54 Percent of Toxicity Chance -
                                      Almost Certainly Toxic
                                    </p>
                                  </template>
                                  <img
                                    :src="showToxicImg(item.toxic)"
                                    style="height: 30px"
                                    alt=""
                                /></a-popover>
                              </li>
                              <li class="report">
                                {{ showSentimentText(item.sentiment)
                                }}<a-popover title="Sentimental">
                                  <template #content>
                                    <p>
                                      Green Similing Face:
                                      <br />
                                      Most Likely Positive
                                    </p>
                                    <p>
                                      Yellow Normal Face:
                                      <br />
                                      Most Likely Neutral
                                    </p>
                                    <p>
                                      Red Sad Face:
                                      <br />
                                      Most Likely Negative
                                    </p>
                                  </template>
                                  <img
                                    :src="showSentimentImg(item.sentiment)"
                                    style="height: 30px; margin-left: 5px"
                                    alt=""
                                /></a-popover>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </el-scrollbar>
                </div>
              </a-tab-pane>

              <a-tab-pane key="twitter" tab="Twitter reviews">
                <div class="comment-div">
                  <div class="section-title">
                    <div class="comment-filter">
                      <h5>Twitter Comment</h5>
                      <div class="filter-select">
                        <a-select
                          placeholder="Filter"
                          style="width: 150px"
                          @change="handleTwitterFilterChange"
                        >
                          <a-select-option value="all">All</a-select-option>
                          <a-select-opt-group>
                            <template #label>
                              <span> Toxic Degree </span>
                            </template>
                            <a-select-option value="notoxic"
                              >Non Toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
                            >
                            <a-select-option value="neutral"
                              >Neutral</a-select-option
                            >
                            <a-select-option value="negative"
                              >Negative</a-select-option
                            >
                          </a-select-opt-group>
                        </a-select>
                      </div>
                    </div>
                  </div>
                  <el-scrollbar max-height="700px">
                    <a-empty v-if="twitterreview.length < 1">
                      <template #description>
                        <span>
                          <!-- Customize -->
                          <a>Sorry, don't have now</a>
                        </span>
                      </template>
                    </a-empty>
                    <div
                      class="comment-wrap"
                      v-for="item in twitterreview"
                      :key="item.id"
                    >
                      <div class="amdb__review__item">
                        <div class="amdb__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="emptyprofile" />
                            </div>
                          </div>
                        </div>
                        <div class="amdb__review__item__text">
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="judgeBadWordOther(item.content)"
                          />
                          <div class="bottom-comment">
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{
                                  "Toxicity rate: " +
                                  changeToPercent(item.toxic) +
                                  showToxicText(item.toxic[0])
                                }}<a-popover title="Toxicity">
                                  <template #content>
                                    <p>
                                      Green Skull:
                                      <br />
                                      0-53 Percent of Toxicity Chance - Most
                                      likely Non-Toxic
                                    </p>
                                    <p>
                                      Red Skull:
                                      <br />
                                      Above 54 Percent of Toxicity Chance -
                                      Almost Certainly Toxic
                                    </p>
                                  </template>
                                  <img
                                    :src="showToxicImg(item.toxic)"
                                    style="height: 30px"
                                    alt=""
                                /></a-popover>
                              </li>
                              <li class="report">
                                {{ showSentimentText(item.sentiment)
                                }}<a-popover title="Sentimental">
                                  <template #content>
                                    <p>
                                      Green Similing Face:
                                      <br />
                                      Most Likely Positive
                                    </p>
                                    <p>
                                      Yellow Normal Face:
                                      <br />
                                      Most Likely Neutral
                                    </p>
                                    <p>
                                      Red Sad Face:
                                      <br />
                                      Most Likely Negative
                                    </p>
                                  </template>
                                  <img
                                    :src="showSentimentImg(item.sentiment)"
                                    style="height: 30px; margin-left: 5px"
                                    alt=""
                                /></a-popover>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </el-scrollbar>
                </div>
              </a-tab-pane>
            </a-tabs>
          </div>
        </div>
        <div class="col-lg-4 col-md-4">
          <div class="amdb__details__sidebar">
            <div class="section-title">
              <h5>you might like...</h5>
            </div>
            <a-empty v-if="recommendationMovies.length < 1">
              <template #description>
                <span>
                  <a>Sorry, No recommendations</a>
                </span>
              </template>
            </a-empty>
            <div
              class="amdb_movies__sidebar__comment__item"
              v-for="item in recommendationMovies"
              :key="item.id"
            >
              <router-link
                :to="{ path: '/movie/' + item.id, query: { id: item.tmdb_Id } }"
              >
                <div class="amdb_movies__sidebar__comment__item__pic">
                  <img
                    class="pichover"
                    :src="moviePoster + item.poster"
                    alt=""
                  />
                </div>
                <div class="amdb_movies__sidebar__comment__item__text">
                  <h5>
                    <a class="twoline-ellipsis" style="color: white">{{
                      item.title
                    }}</a>
                  </h5>
                  <ul>
                    <li
                      v-for="genre in item.genres[0].slice(0, 2)"
                      :key="genre.id"
                    >
                      {{ genre.name }}
                    </li>
                  </ul>
                  <div class="ep">{{ item.vote_average + "/ 10" }}</div>
                  <span><i class="fa fa-eye"></i> {{ item.release_date }}</span>
                </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template> 

<script>
import { ref, onBeforeMount, computed, h, onMounted } from "vue";
import { useRoute } from "vue-router";
import router from "@/router";
import { useStore } from "vuex";
import { YoutubeVue3 } from "youtube-vue3";
import { message } from "ant-design-vue";
import { SmileOutlined, QuestionCircleOutlined } from "@ant-design/icons-vue";
import { notification } from "ant-design-vue";
import { ElMessageBox } from "element-plus";
import env from "@/env.js";
import ToolMethod from "../tools.js";
import UserApi from "../services/user.service";

import {
  LikeFilled,
  LikeOutlined,
  DislikeFilled,
  DislikeOutlined,
} from "@ant-design/icons-vue";

export default {
  components: {
    LikeFilled,
    LikeOutlined,
    DislikeFilled,
    DislikeOutlined,
    YoutubeVue3,
    QuestionCircleOutlined,
  },

  setup() {
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);
    const movie = ref({});
    const casts = ref({});
    const castList = ref([]);
    const castDetail = ref({});
    const start = ref(0);
    const route = useRoute();
    const movieid = ref("");
    const imdbmovieid = ref("");
    const activeKey = ref("amdb");
    const popToxicText = ref("");
    const popSentimentText = ref("");
    const popHightToxicText = ref("");
    const commentConfirmLoading = ref(false);
    const addCommentsDialog = ref(false);
    const reportCommentsDialog = ref(false);
    const tmdbreview = ref([]);
    const tmdbAllreview = ref([]);
    const amdbreview = ref([]);
    const amdbAllreview = ref([]);
    const imdbreview = ref([]);
    const imdbAllreview = ref([]);
    const youtubereview = ref([]);
    const youtubeAllreview = ref([]);
    const twitterreview = ref([]);
    const twitterAllreview = ref([]);
    const recommendationMovies = ref([]);
    const moviePoster = ref("");
    const video_id = ref("");
    const emptyprofile = ref("");
    const isShowTrailer = ref(false);
    const trailerWidth = ref(700);
    const commentLoading = ref(false);
    const isShowCastDetail = ref(false);
    const AMDBAPI = ref(env.AMDBAPI);
    let reportCommentId = "";
    let crewList = [];
    let youtube = ref(null);
    moviePoster.value = env.tmdbpic;
    movieid.value = route.params.id;
    emptyprofile.value =
      "https://img1.sc115.com/uploads/sc/jpg/HD/49/21850.jpg";
    //comments
    const comments = ref([]);
    const submitting = ref(false);
    const commentsValue = ref("");
    onBeforeMount(async () => {
      // fetch movie detail
      await UserApi.getMovieDetail(movieid.value).then((response) => {
        movie.value = response.data;
        start.value = movie.value.vote_average / 2;
        imdbmovieid.value = response.data.imdb_id;
      });

      // Fetch recommendation movies
      UserApi.getRecommandationById(movieid.value)
        .then((response) => {
          const randomMovie = response.data.data;
          if (randomMovie.length) {
            recommendationMovies.value = ToolMethod.RandomNumBoth(
              randomMovie,
              randomMovie.length > 4 ? 5 : randomMovie.length
            );
          }
        })
        .catch((error) => {
          showErroeMessage();
        });

      // Fetch setRecommendation
      UserApi.setRecommendation(
        movieid.value,
        currentUser.value === null ? "" : currentUser.value.data.userId,
        movie.value.genres[0].id
      )
        .then((response) => {
        })
        .catch((error) => {
          showErroeMessage();
        });

      //Fetch trailer
      UserApi.getMovieTrailer(movieid.value).then((response) => {
        const video = response.data.results;
        // TODO no videos
        video_id.value = video[0].key;
      });

      //Fetch casts
      UserApi.getMovieCasts(movieid.value).then((response) => {
        casts.value = response.data;
        crewList = casts.value.crew;
        addCrewToCast();
        if (response.data.cast.length <= 6) {
          castList.value = castList.value.concat(casts.value.cast);
        } else {
          castList.value = castList.value.concat(casts.value.cast.slice(0, 6));
        }
      });
      getAMDBComments();
    });

    onMounted(() => {
      (function (d, s, id) {
        var js,
          fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s);
        js.id = id;
        js.src =
          "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
        fjs.parentNode.insertBefore(js, fjs);
      })(document, "script", "facebook-jssdk");

      window.fbAsyncInit = function () {
        var appId = "903265547247503";
        FB.init({
          appId: appId,
          xfbml: true,
          version: "v2.9",
        });
      };

      // FB Share with custom OG data.
      (function ($) {
        $(".fb_share_btn").on("click", function (event) {
          event.preventDefault();
          event.stopImmediatePropagation();

          FB.ui({
            method: "feed",
            name: "Facebook Dialogs",
            link: "http://amdbmovie.com/movie/" + movieid.value,
            picture: "http://fbrell.com/f8.jpg",
            caption: "wwwwwwwwwwwwwwwwwww",
            description: "yyyyyyyyyyyyyyyyyyyy",
          });
        });
      })(jQuery);

      window.onresize = () => {
        let w = window.innerWidth;
        if (w > 700) {
          trailerWidth.value = 700;
        } else {
          trailerWidth.value = w - 10;
        }
      };
    });

    /**
     * Get AMDB comments.
     */
    const getAMDBComments = () => {
      commentLoading.value = true;
      //Fetch AMDB Comments
      UserApi.getMovieComments(movieid.value)
        .then((response) => {
          amdbreview.value = response.data.data;
          amdbAllreview.value = response.data.data;
          commentLoading.value = false;
        })
        .catch((error) => {
          showErroeMessage();
          commentLoading.value = false;
        });
    };

    /**
     * Add  Director to cast list.
     */
    const addCrewToCast = () => {
      for (let item of crewList) {
        if (item.job == "Director") {
          castList.value.push(item);
        }
      }
    };

    const handleCancel = () => {
      isShowTrailer.value = false;
    };

    const showToxicText = (rate) => {
      return ToolMethod.showToxicText(rate);
    };

    /**
     * Show toxic image
     * @rate  toxic rate.
     */
    const showToxicImg = (rate) => {
      if (rate > 0.54) {
        return require("@/assets/toxic-red.png");
      } else {
        return require("@/assets/toxic-green.png");
      }
    };

    /**
     * Show sentiment image
     * @rate  sentiment rate.
     */
    const showSentimentImg = (rate) => {
      if (rate < 0.5) {
        return require("@/assets/sentiment-red.png");
      } else if (rate > 0.5 && rate < 1.5) {
        return require("@/assets/sentiment-green.png");
      } else {
        return require("@/assets/sentiment-yellow.png");
      }
    };

    const showSentimentText = (rate) => {
      return ToolMethod.showSentimentText(rate);
    };

    const formatDate = (value) => {
      return ToolMethod.formatDate(value);
    };

    const changeToPercent = (value) => {
      return ToolMethod.changeToPercent(value);
    };

    const showErroeMessage = () => {
      return message.error("Server is busy, try again later");
    };

    /**
     * Change tab function.
     * @value  tab name
     */
    const changeCommentTab = (value) => {
      commentLoading.value = true;
      switch (value) {
        case "tmdb": //Fetch TMDB Comments
          if (tmdbAllreview.value.length > 0) {
            commentLoading.value = false;
            return;
          }
          UserApi.getTmdbComments(movieid.value)
            .then((response) => {
              if (response.data.data.reviews) {
                tmdbreview.value = response.data.data.reviews[0];
                tmdbAllreview.value = response.data.data.reviews[0];
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              showErroeMessage();
              commentLoading.value = false;
            });

          break;
        case "imdb":
          if (imdbAllreview.value.length > 0) {
            commentLoading.value = false;
            return;
          }
          //Fetch IMDB Comments
          UserApi.getImdbComments(imdbmovieid.value)
            .then((response) => {
              if (response.data.data.reviews.items) {
                imdbreview.value = response.data.data.reviews.items;
                imdbAllreview.value = response.data.data.reviews.items;
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              showErroeMessage();
              commentLoading.value = false;
            });
          break;
        case "youtube":
          if (youtubeAllreview.value.length > 0) {
            commentLoading.value = false;
            return;
          }
          //Fetch Youtube Comments
          UserApi.getYoutubeComments(movie.value.original_title, movieid.value)
            .then((response) => {
              if (response.data.data) {
                youtubereview.value = response.data.data;
                youtubeAllreview.value = response.data.data;
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              showErroeMessage();
              commentLoading.value = false;
            });
          break;
        case "twitter":
          if (twitterAllreview.value.length > 0) {
            commentLoading.value = false;
            return;
          }
          //Fetch Twitter Comments
          UserApi.getTwitterComments(movie.value.original_title, movieid.value)
            .then((response) => {
              if (response.data.data) {
                twitterreview.value = response.data.data;
                twitterAllreview.value = response.data.data;
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              showErroeMessage();
              commentLoading.value = false;
            });
          break;
        default:
          commentLoading.value = false;
        // code block
      }
    };

    /**
     * Check before post comment.
     */
    const handleSubmit = () => {
      if (!authLogin() || !commentsValue.value) {
        return;
      }
      //  Comment detectaddCommentsDialog
      commentConfirmLoading.value = true;
      popToxicText.value = "";
      popSentimentText.value = "";
      popHightToxicText.value = "";
      UserApi.detectUserComment(commentsValue.value).then((response) => {
        const commentStatus = response.data.data;
        addCommentsDialog.value = true;
        popToxicText.value =
          "Toxic is " +
          showToxicText(commentStatus.toxic[0]) +
          "(" +
          Number(commentStatus.toxic[0] * 100).toFixed(1) +
          "%)";
        popSentimentText.value =
          "Sentiment is " + showSentimentText(commentStatus.sentiment[0]);
        commentConfirmLoading.value = false;
        if (commentStatus.toxic[0] > 0.54) {
          popHightToxicText.value =
            "Your comment is maybe TOXIC. If you post too much, the administrator will block your account.";
        }
      });
    };

    /**
     *  Post comments.
     */
    const confirmAddComment = () => {
      commentLoading.value = true;
      addCommentsDialog.value = false;

      const postFormData = new FormData();
      postFormData.append("movieId", movieid.value);
      postFormData.append("comment", commentsValue.value);
      postFormData.append("userId", currentUser.value.data.userId);
      // Post comments
      UserApi.postUserComment(postFormData).then((response) => {
        // tmdbreview.value = response.data;
        submitting.value = false;
        commentsValue.value = "";
        commentLoading.value = false;
        if (response.data.code === 200) {
          getAMDBComments();
          notification.open({
            duration: 2,
            message: "Add comment successfully!",
            icon: h(SmileOutlined, {
              style: "color: #108ee9",
            }),
          });
        } else {
          ElMessageBox.confirm(response.data.msg, "Warning", {
            cancelButtonText: "Cancel",
            type: "warning",
            center: true,
          });
        }
      });
      addCommentsDialog.value = false;
    };

    const cancelAddComment = () => {
      return ToolMethod.changeToPercent(value);
    };

    const ShowTrailer = () => {
      isShowTrailer.value = true;
      if (video_id.value.length < 1) {
        message.error("Sorry, trailer is not available now!");
      }
    };

    const showCastDetail = (id) => {
      isShowCastDetail.value = true;
      //Fetch Cast Detials
      UserApi.getMovieCastsDetail(id).then((response) => {
        castDetail.value = response.data;
      });
    };

    //AMDB filter change
    const handleFilterChange = (value) => {
      amdbreview.value = commentsFilter(amdbAllreview.value, value);
    };

    //TMDB filter change
    const handleTMDBFilterChange = (value) => {
      tmdbreview.value = commentsFilter2(tmdbAllreview.value, value);
    };

    //IMDB filter change
    const handleIMDBFilterChange = (value) => {
      imdbreview.value = commentsFilter2(imdbAllreview.value, value);
    };

    //Youtube filter change
    const handleYoutubeFilterChange = (value) => {
      youtubereview.value = commentsFilter2(youtubeAllreview.value, value);
    };

    //Twitter filter change
    const handleTwitterFilterChange = (value) => {
      twitterreview.value = commentsFilter2(twitterAllreview.value, value);
    };

    /**
     * Filter function based on toxic or sentiment label.
     * @value  data
     * @filter label
     */
    const commentsFilter = (value, filter) => {
      let comments = [];
      if (filter === "notoxic") {
        for (let i of value) {
          if (i.toxic <= 0.54) {
            comments.push(i);
          }
        }
      } else if (filter === "toxic") {
        for (let i of value) {
          if (i.toxic > 0.54) {
            comments.push(i);
          }
        }
      } else if (filter === "positive") {
        for (let i of value) {
          if (i.sentiment > 0.5 && i.sentiment < 1.5) {
            comments.push(i);
          }
        }
      } else if (filter === "negative") {
        for (let i of value) {
          if (i.sentiment < 0.5) {
            comments.push(i);
          }
        }
      } else if (filter === "neutral") {
        for (let i of value) {
          if (i.sentiment > 1.5) {
            comments.push(i);
          }
        }
      } else {
        comments = value;
      }
      return comments;
    };
    /**
     * Filter function based on toxic or sentiment label.
     * @value  data
     * @filter label
     */
    const commentsFilter2 = (value, filter) => {
      let comments = [];
      if (filter === "notoxic") {
        for (let i of value) {
          if (i.toxic[0] <= 0.54) {
            comments.push(i);
          }
        }
      } else if (filter === "toxic") {
        for (let i of value) {
          if (i.toxic[0] > 0.54) {
            comments.push(i);
          }
        }
      } else if (filter === "positive") {
        for (let i of value) {
          if (i.sentiment > 0.5 && i.sentiment < 1.5) {
            comments.push(i);
          }
        }
      } else if (filter === "negative") {
        for (let i of value) {
          if (i.sentiment < 0.5) {
            comments.push(i);
          }
        }
      } else if (filter === "neutral") {
        for (let i of value) {
          if (i.sentiment > 1.5) {
            comments.push(i);
          }
        }
      } else {
        comments = value;
      }
      return comments;
    };

    /**
     * Add to like list
     */
    const addLikeList = () => {
      if (!authLogin()) {
        return;
      }
      UserApi.addLikeList(movieid.value, currentUser.value.data.userId).then(
        (response) => {
          if (response.data.code == 200) {
            notification.open({
              duration: 2,
              message: "Add like list successfully!",
              icon: h(SmileOutlined, {
                style: "color: #108ee9",
              }),
            });
          } else {
            notification.open({
              duration: 2,
              message: "Already add !!",
            });
          }
        }
      );
    };

    /**
     * Report AMDB comments
     * @item  data
     */
    const amdbReport = (item) => {
      if (!authLogin()) {
        return;
      }
      reportCommentId = item.id;
      reportCommentsDialog.value = true;
    };

    const confirmReportComment = () => {
      // report comments
      UserApi.reportComment(reportCommentId, currentUser.value.data.userId)
        .then((response) => {
          reportCommentsDialog.value = false;
          if (response.data.code === 200) {
            message.success("Thanks for your report!");
          }
        })
        .catch((error) => {
          reportCommentsDialog.value = false;
          showErroeMessage();
        });
    };

    /**
     * Check wheth need to login
     */
    const authLogin = () => {
      if (!localStorage.getItem("user")) {
        router.push({
          name: "Login",
        });
        return false;
      } else {
        return true;
      }
    };

    const judgeBadWord = (str) => {
      return ToolMethod.judgeBadWord(str);
    };

    const judgeBadWordOther = (str) => {
      return ToolMethod.judgeBadWordOther(str);
    };

    /**
     * Check img url.
     * @item  data
     */
    const linkCheck = (item) => {
      return item.includes("http");
    };

    /**
     * Format img url.
     * @item  data
     */
    const checkLink = (item) => {
      return item.slice(1, item.length);
    };

    return {
      movie,
      start,
      casts,
      moviePoster,
      video_id,
      imdbmovieid,
      movieid,
      youtube,
      isShowTrailer,
      emptyprofile,
      castList,
      popToxicText,
      popHightToxicText,
      popSentimentText,
      commentConfirmLoading,
      addCommentsDialog,
      reportCommentsDialog,
      activeKey,
      commentLoading,
      recommendationMovies,
      currentUser,
      AMDBAPI,
      // comments
      comments,
      submitting,
      commentsValue,
      tmdbreview,
      imdbreview,
      amdbreview,
      youtubereview,
      twitterreview,
      castDetail,
      isShowCastDetail,
      trailerWidth,
      ellipsis: ref(true),
      judgeBadWord,
      linkCheck,
      checkLink,
      judgeBadWordOther,
      amdbReport,
      handleCancel,
      handleSubmit,
      showCastDetail,
      ShowTrailer,
      showToxicText,
      showSentimentText,
      cancelAddComment,
      confirmAddComment,
      confirmReportComment,
      changeToPercent,
      showToxicImg,
      showSentimentImg,
      formatDate,
      addLikeList,
      handleFilterChange,
      handleTMDBFilterChange,
      handleIMDBFilterChange,
      handleYoutubeFilterChange,
      handleTwitterFilterChange,
      changeCommentTab,
    };
  },
};
</script>

<style lang="scss" >
/*---------------------
   Details
-----------------------*/

.ep {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  padding: 2px 12px;
  margin-bottom: 10px;
  border-radius: 4px;
}
.notrailer {
  color: #fff;
}
.amdb_movies__sidebar__comment__item__text ul {
  padding-left: 0 !important;
}
.amdb-details {
  padding-top: 60px;
}

.amdb__details__content {
  margin-bottom: 65px;
}

.amdb__details__text {
  position: relative;
}

.amdb__details__text p {
  color: #b7b7b7;
  font-size: 18px;
  line-height: 30px;
}

.amdb__details__pic {
  max-height: 440px;
  border-radius: 5px;
  position: relative;
}

.amdb__details__pic .comment {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  bottom: 25px;
}

.amdb__details__pic .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  bottom: 25px;
}

.amdb__details__title {
  margin-bottom: 20px;
  padding-right: 100px;
}

.amdb__details__title h3 {
  color: #fff;
  font-weight: 700;
  margin-bottom: 13px;
}

.amdb__details__title span {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
}

.amdb__details__rating {
  text-align: center;
  position: absolute;
  right: 0;
  top: 0;
}

.rating {
  margin-left: 5px;
  font-size: 24px;
  color: #e89f12;
  display: inline-block;
}

.amdb__details__rating span {
  display: block;
  font-size: 18px;
}

.amdb__details__widget {
  margin-bottom: 15px;
}

.amdb__details__widget ul {
  margin-bottom: 20px;
}

.amdb__details__widget ul li {
  list-style: none;
  font-size: 15px;
  color: #ffffff;
  line-height: 30px;
  position: relative;
  padding-left: 18px;
}

.amdb__details__widget ul li:before {
  position: absolute;
  left: 0;
  top: 12px;
  height: 6px;
  width: 6px;
  background: #b7b7b7;
  content: "";
}

.amdb__details__widget ul li span {
  color: #b7b7b7;
  width: 115px;
  display: inline-block;
}

.amdb__details__btn .follow-btn {
  font-size: 10px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px;
  margin-right: 11px;
  margin-bottom: 13px;
}

.amdb__details__btn .watch-btn span {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px 0 0 4px;
  margin-right: 1px;
}

.amdb__details__btn .watch-btn i {
  font-size: 20px;
  display: inline-block;
  background: #e53637;
  padding: 11px 5px 16px 8px;
  color: #ffffff;
  border-radius: 0 4px 4px 0;
}

.amdb__details__review {
  margin-bottom: 55px;
  .comment-filter {
    .filter-select {
      position: absolute;
      right: 15px;
      top: 70px;
    }
  }
}

.amdb__review__item {
  overflow: hidden;
  margin-bottom: 15px;
  .bottom-comment {
    margin-top: 10px;
    color: #acb4c2;
    font-size: 0.875rem;
  }
  .comment-date {
    float: left;
  }
  .comment-actions {
    float: right;
  }
  .comment-actions li {
    display: inline;
  }
  .comment-actions li.toxicrate {
    padding-right: 5px;
    border-right: 1px solid #e1e5eb;
  }
  .comment-actions li.sentiemnt-rate {
    padding-left: 5px;
    padding-right: 5px;
    border-right: 1px solid #e1e5eb;
  }
  .comment-actions li.report {
    padding-left: 0.625rem;
  }
}

.amdb__review__item__pic {
  float: left;
  margin-right: 20px;
  position: relative;
}

.amdb__review__item__pic:before {
  position: absolute;
  right: -30px;
  top: 15px;
  border-top: 15px solid transparent;
  border-left: 15px solid #494a58;
  content: "";
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

.amdb__review__item__pic img {
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.amdb__review__item__text {
  overflow: hidden;
  background: #494a58;
  padding: 13px 30px 0px 20px;
  border-radius: 10px;

  .comment-text {
    color: #fff;
  }
}

.amdb__review__item__text h6 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 10px;
}

.amdb__review__item__text h6 span {
  color: #b7b7b7;
  font-weight: 400;
}

.amdb__review__item__text p {
  color: #b7b7b7;
  line-height: 23px;
  margin-bottom: 0;
}

.amdb__details__form form textarea {
  width: 100%;
  font-size: 15px;
  color: #b7b7b7;
  padding-left: 20px;
  padding-top: 12px;
  height: 110px;
  border: none;
  border-radius: 5px;
  resize: none;
  margin-bottom: 24px;
}

.amdb__details__form form button {
  font-size: 11px;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  background: #e53637;
  border: none;
  padding: 10px 15px;
  border-radius: 2px;
}

.movie-casts {
  display: flex;
  flex-wrap: wrap;
}

.comment-div-amdb {
  // border: #e53637 Dashed 1px;
  box-shadow: 0 2px 12px 0 rgba(236, 230, 230, 0.1);
  padding: 15px 15px 0 15px;
  border-radius: 15px;
  background-color: #1f1d1d;
}

.comment-div {
  // border: #e53637 Dashed 1px;
  box-shadow: 0 2px 12px 0 rgba(236, 230, 230, 0.1);
  padding: 15px;
  border-radius: 15px;
  background-color: #1f1d1d;
}

@media only screen and (max-width: 800px) {
  .filter-select {
    position: initial !important;
    margin-top: 30px;
  }
}

@media only screen and (max-width: 600px) {
  .amdb-details {
    padding-top: 20px !important;
  }
  .amdb__details__pic {
    height: 250px !important;
  }
  .amdb__details__title {
    padding-right: 0 !important;
  }
  .amdb__details__text p {
    font-size: 15px !important;
  }
}
</style>