 <template>
  <section class="anime-details spad">
    <div class="">
      <a-modal
        :visible="isShowTrailer"
        :maskClosable="true"
        :closable="false"
        :footer="null"
        :destroyOnClose="true"
        :width="700"
        @cancel="handleCancel"
      >
        <YoutubeVue3
          ref="youtube"
          :videoid="video_id"
          :width="700"
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
      <div class="anime__details__content">
        <div class="row">
          <div class="col-lg-3">
            <div class="anime__details__pic set-bg">
              <img
                :src="moviePoster + movie.poster_path"
                alt="Movie Poster"
                class="anime__details__pic set-bg"
                @click="isShowTrailer = true"
              />
            </div>
          </div>
          <div class="col-lg-9">
            <div class="anime__details__text">
              <div class="anime__details__title">
                <h3>{{ movie.original_title }}</h3>
                <span>{{ movie.release_date }}</span>
              </div>
              <div class="anime__details__rating">
                <div class="rating">
                  <a-rate v-model:value="start" disabled allowHalf />
                  <p>{{ movie.vote_average }}</p>
                  <!-- <a-rate v-model:value="start" disabled allowHalf /> -->
                  <!-- <p>{{ movie.vote_average }}</p> -->
                </div>
              </div>

              <p style="font-size: 20px">{{ movie.overview }}</p>

              <div class="anime__details__widget">
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
                          Cancle
                        </el-button>
                      </span>
                    </template>
                  </el-dialog>
                </div>
              </div>
              <div class="anime__details__btn">
                <a @click="addLikeList()" class="follow-btn">
                  <i class="fa fa-heart"></i> ADD Like list
                </a>
                <a @click="isShowTrailer = true" class="follow-btn"
                  ><i class="fa fa-play"></i> <span>Watch trailer</span>
                </a>
                <a class="follow-btn fb_share_btn"
                  ><i class="fab fa-facebook"></i>
                  <span> Facebook Share</span>
                </a>
                <!-- <div class="share-function">
                  <div id="fb-root">
                    <div
                      class="fb-share-button"
                      data-href="http://amdb-frontend.s3-website-eu-west-1.amazonaws.com/main/home/maindisplay"
                      data-layout="button_count"
                    ></div>
                    <div class="fb_share_btn">button</div>
                  </div> -->

                <!-- <a
                    href="javascript:window.open('http://www.facebook.com/sharer.php?u='+encodeURIComponent('https://alexey-avdeev.com/vanilla-sharing/')+'&title=' +encodeURIComponent('HALLO'))"
                    style="font-size: 14px; margin-right: 50px"
                  >
                    分享Facebook
                  </a> -->

                <!-- <a
                    href="javascript:window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent('https://alexey-avdeev.com/vanilla-sharing/')+'&title=' +encodeURIComponent('HALLO'))"
                    style="font-size: 14px; margin-right: 50px"
                  >
                    分享T -->
                <!-- </a> -->
                <!-- </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-8 col-md-8">
          <div class="anime__details__review">
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
                              >Non toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                            <a-select-option value="severetoxic"
                              >Severe toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
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
                      <div class="anime__review__item">
                        <div class="anime__review__item__pic">
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
                        <div class="anime__review__item__text">
                          <h6 class="comment-author">
                            {{ item.userName }}
                          </h6>
                          <!-- <p class="comment-text">{{ item.comment }}</p> -->
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            v-html="judgeBadWord(item.comment)"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">
                              {{ formatDate(item.createTime) }}
                            </div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{ showToxicText(item.toxic) }} :
                                {{ changeToPercent(item.toxic) }}
                                <img
                                  :src="showToxicImg(item.toxic)"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentiemntText(item.sentiment) }} :
                                {{ changeToPercent(item.sentiment) }}
                                <img
                                  :src="showSentimentImg(item.sentiment)"
                                  style="height: 30px"
                                  alt=""
                                />
                                <!-- <img
                              src="../assets/toxic-red.png"
                              style="height: 30px"
                              alt=""
                            /> -->
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
                  <div class="anime__details__form">
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
                          <a-textarea v-model:value="commentsValue" :rows="4" />
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
                          <!-- </a-popconfirm> -->
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
                              >Non toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                            <a-select-option value="severetoxic"
                              >Severe toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
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
                      <div class="anime__review__item">
                        <div class="anime__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar
                                :src="
                                  item.author_details.avatar_path
                                    ? moviePoster +
                                      item.author_details.avatar_path
                                    : emptyprofile
                                "
                              />
                            </div>
                          </div>
                        </div>
                        <div class="anime__review__item__text">
                          <h6 class="comment-author">{{ item.author }}</h6>
                          <!-- <p class="comment-text">{{ item.content }}</p> -->
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="item.content"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">
                              {{ item.created_at }}
                            </div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{ showToxicText(item.toxic[0]) }}:{{
                                  changeToPercent(item.toxic)
                                }}
                                <img
                                  :src="showToxicImg(item.toxic)"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentiemntText(item.sentiment[0]) }} :
                                {{ changeToPercent(item.sentiment[0]) }}
                                <img
                                  :src="showSentimentImg(item.sentiment[0])"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <!-- <li class="report">Report</li> -->
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
                              >Non toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                            <a-select-option value="severetoxic"
                              >Severe toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
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
                      <div class="anime__review__item">
                        <div class="anime__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="emptyprofile" />
                            </div>
                          </div>
                        </div>
                        <div class="anime__review__item__text">
                          <h6 class="comment-author">{{ item.username }}</h6>
                          <!-- <p class="comment-text">{{ item.content }}</p> -->
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="item.content"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">{{ item.date }}</div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{ showToxicText(item.toxic[0]) }}:{{
                                  changeToPercent(item.toxic)
                                }}
                                <img
                                  :src="showToxicImg(item.toxic)"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentiemntText(item.sentiment[0]) }} :
                                {{ changeToPercent(item.sentiment[0]) }}
                                <img
                                  :src="showSentimentImg(item.sentiment[0])"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <!-- <li class="report">Report</li> -->
                              <li class="report">
                                {{
                                  item.warningSpoilers ? "warningSpoilers" : ""
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
                              >Non toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                            <a-select-option value="severetoxic"
                              >Severe toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
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
                      <div class="anime__review__item">
                        <div class="anime__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="item.profile_picture" />
                            </div>
                          </div>
                        </div>
                        <div class="anime__review__item__text">
                          <h6 class="comment-author">{{ item.username }}</h6>
                          <!-- <p class="comment-text">{{ item.review }}</p> -->
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="item.review"
                          />
                          <div class="bottom-comment">
                            <div class="comment-date">{{ item.time }}</div>
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{ showToxicText(item.toxic[0]) }}:{{
                                  changeToPercent(item.toxic)
                                }}
                                <img
                                  :src="showToxicImg(item.toxic)"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentiemntText(item.sentiment[0]) }} :
                                {{ changeToPercent(item.sentiment[0]) }}
                                <img
                                  :src="showSentimentImg(item.sentiment[0])"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <!-- <li class="report">Report</li> -->
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
                              >Non toxic</a-select-option
                            >
                            <a-select-option value="toxic"
                              >Toxic</a-select-option
                            >
                            <a-select-option value="severetoxic"
                              >Severe toxic</a-select-option
                            >
                          </a-select-opt-group>
                          <a-select-opt-group>
                            <template #label>
                              <span> Sentiment Degree </span>
                            </template>
                            <a-select-option value="positive"
                              >Positive</a-select-option
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
                      <div class="anime__review__item">
                        <div class="anime__review__item__pic">
                          <div class="photo-avatar">
                            <div class="avatar">
                              <a-avatar :src="emptyprofile" />
                            </div>
                          </div>
                        </div>
                        <div class="anime__review__item__text">
                          <!-- <h6 class="comment-author">{{ item.username }}</h6> -->
                          <!-- <p class="comment-text">{{ item.content }}</p> -->
                          <a-typography-paragraph
                            class="comment-text"
                            :ellipsis="
                              ellipsis
                                ? { rows: 5, expandable: true, symbol: 'more' }
                                : false
                            "
                            :content="item.content"
                          />
                          <div class="bottom-comment">
                            <!-- <div class="comment-date">{{ item.time }}</div> -->
                            <ul class="comment-actions">
                              <li class="toxicrate">
                                {{ showToxicText(item.toxic[0]) }}:{{
                                  changeToPercent(item.toxic)
                                }}
                                <img
                                  :src="showToxicImg(item.toxic)"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <li class="sentiemnt-rate">
                                {{ showSentiemntText(item.sentiment[0]) }} :
                                {{ changeToPercent(item.sentiment[0]) }}
                                <img
                                  :src="showSentimentImg(item.sentiment[0])"
                                  style="height: 30px"
                                  alt=""
                                />
                              </li>
                              <!-- <li class="report">Report</li> -->
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
          <div class="anime__details__sidebar">
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
              class="product__sidebar__comment__item"
              v-for="item in recommendationMovies"
              :key="item.id"
            >
              <router-link
                :to="{ path: '/movie/' + item.id, query: { id: item.tmdb_Id } }"
                @click.native="fleshMovie"
              >
                <div class="product__sidebar__comment__item__pic">
                  <img
                    class="pichover"
                    :src="moviePoster + item.poster"
                    alt=""
                  />
                </div>
                <div class="product__sidebar__comment__item__text">
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
import { ref, inject, onBeforeMount, computed, h, onMounted } from "vue";
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
    const axios = inject("axios"); // inject axios
    const store = useStore();
    const currentUser = computed(() => store.state.auth.user);
    const movie = ref({});
    const casts = ref({});
    const castList = ref([]);
    let crewList = [];
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
    const commentLoading = ref(false);
    const isShowCastDetail = ref(false);
    const AMDBAPI = ref(env.AMDBAPI);
    let youtube = ref(null);
    moviePoster.value = env.tmdbpic;
    movieid.value = route.params.id;
    emptyprofile.value =
      "https://img1.sc115.com/uploads/sc/jpg/HD/49/21850.jpg";
    //comments
    const comments = ref([]);
    const submitting = ref(false);
    const commentsValue = ref("");
    onBeforeMount(() => {
      // fetch movie detail
      axios
        .get(env.tmdbmovieapi + movieid.value + "?" + env.tmdbkey)
        .then((response) => {
          movie.value = response.data;
          console.log("movie detail");
          console.log(movie.value);
          start.value = movie.value.vote_average / 2;
          console.log("start.value");
          console.log(start.value);
          console.log("imdbmovieid");
          imdbmovieid.value = response.data.imdb_id;
          console.log(imdbmovieid.value);
          console.log("imdbmovie title");
          console.log(movie.value.original_title);

          // Fetch recommendation movies
          axios
            .get(
              env.AMDBAPI + "rec/getRecommendationById?movieId=" + movieid.value
            )
            .then((response) => {
              console.log("getRecommadationById");
              console.log(response.data);
              recommendationMovies.value = response.data.data;
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
              showErroeMessage();
            });
        });

      // Fetch setRecommandation
      axios
        .get(
          env.AMDBAPI +
            "rec/setRecommandation?movieId=" +
            movieid.value +
            "&userId=" +
            (currentUser.value === null ? "" : currentUser.value.data.userId)
        )
        .then((response) => {
          console.log("setRecommandation");
          console.log(response.data);
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });

      //Fetch trailer
      axios
        .get(
          env.tmdbmovieapi +
            movieid.value +
            env.tmdbvideo +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          const video = response.data.results;
          console.log("video_id");
          console.log(video);
          // TODO no videos
          video_id.value = video[0].key;
          console.log(video_id.value);
        });

      //Fetch casts
      axios
        .get(
          env.tmdbmovieapi +
            movieid.value +
            env.tmdbcredits +
            env.tmdbkey +
            env.tmdbtail
        )
        .then((response) => {
          casts.value = response.data;
          console.log("casts detail");
          console.log(casts.value);
          crewList = casts.value.crew;
          addCrewToCast();
          if (response.data.cast.length <= 6) {
            castList.value = castList.value.concat(casts.value.cast);
          } else {
            castList.value = castList.value.concat(
              casts.value.cast.slice(0, 6)
            );
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
            link:
              "http://amdb-frontend.s3-website-eu-west-1.amazonaws.com/movie/" +
              movieid.value,
            picture: "http://fbrell.com/f8.jpg",
            caption: "wwwwwwwwwwwwwwwwwww",
            description: "yyyyyyyyyyyyyyyyyyyy",
          });
        });
      })(jQuery);
    });

    const getAMDBComments = () => {
      commentLoading.value = true;
      //Fetch AMDB Comments
      axios
        .get(
          env.AMDBAPI + "comments/showComments?movieId=" + movieid.value
          // "&userId=" +
          // currentUser.value.data.userId,
        )
        .then((response) => {
          amdbreview.value = response.data.data;
          amdbAllreview.value = response.data.data;
          console.log("amdbreview detail");
          console.log(response.data);
          console.log(amdbreview.value);
          commentLoading.value = false;
        })
        .catch((error) => {
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
          commentLoading.value = false;
        });
    };

    const addCrewToCast = () => {
      console.log("crewList");
      console.log(crewList);
      for (let item of crewList) {
        if (item.job == "Director") {
          console.log("Director");
          console.log(item);
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

    const showToxicImg = (rate) => {
      if (rate > 0 && rate <= 0.53) {
        return require("@/assets/toxic-green.png");
      } else if (rate > 0.53 && rate < 0.9) {
        return require("@/assets/toxic-yellow.png");
      } else {
        return require("@/assets/toxic-red.png");
      }
      // return ToolMethod.showToxicImg(rate);
    };

    const showSentimentImg = (rate) => {
      if (rate > 0.5) {
        return require("@/assets/sentiment-green.png");
      } else {
        return require("@/assets/sentiment-red.png");
      }
      // return ToolMethod.showToxicImg(rate);
    };

    const showSentiemntText = (rate) => {
      return ToolMethod.showSentiemntText(rate);
    };

    const formatDate = (value) => {
      return ToolMethod.formatDate(value);
    };

    const changeToPercent = (value) => {
      return ToolMethod.changeToPercent(value);
    };

    const showErroeMessage = () => {
      return message.error("Sorry, error accured in server");
    };

    const changeCommentTab = (value) => {
      console.log("changeCommentTab");
      console.log(value);
      console.log(tmdbAllreview.value.length);
      console.log(tmdbAllreview.value.length > 0);
      commentLoading.value = true;
      switch (value) {
        case "tmdb": //Fetch TMDB Comments
          if (tmdbAllreview.value.length > 0) {
            commentLoading.value = false;
            return;
          }
          axios
            .get(
              env.AMDBAPI +
                "movieTmdb/movieTmdbReviews?movieId=" +
                movieid.value
            )
            .then((response) => {
              if (response.data.data.reviews) {
                tmdbreview.value = response.data.data.reviews[0];
                tmdbAllreview.value = response.data.data.reviews[0];
              }
              console.log("tmdbreview detail");
              console.log(tmdbreview.value);
              commentLoading.value = false;
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
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
          axios
            .get(
              env.AMDBAPI +
                "movieImdb/movieImdbReviews?movieId=" +
                imdbmovieid.value
            )
            .then((response) => {
              if (response.data.data.reviews.items) {
                imdbreview.value = response.data.data.reviews.items;
                imdbAllreview.value = response.data.data.reviews.items;
                console.log("imdbreview detail");
                console.log(imdbreview.value);
                console.log(response.data.data.reviews.items);
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
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
          axios
            .get(
              env.AMDBAPI +
                "movieYoutube/movieYoutubeReviews?movieName=" +
                movie.value.original_title +
                "&movieId=" +
                movieid.value
            )
            .then((response) => {
              if (response.data.data) {
                youtubereview.value = response.data.data;
                youtubeAllreview.value = response.data.data;
                console.log("youtubereview detail");
                console.log(youtubereview.value);
                console.log(response.data.data);
              }
              commentLoading.value = false;
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
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
          axios
            .get(
              env.AMDBAPI +
                "movieTwitter/movieTwitterReviews?movieName='" +
                movie.value.original_title +
                "'&movieId=" +
                movieid.value
            )
            .then((response) => {
              if (response.data.data) {
                twitterreview.value = response.data.data;
                twitterAllreview.value = response.data.data;
              }
              console.log("twitterreview detail");
              console.log(response);
              console.log(response.data.data);
              console.log(twitterreview.value);
              commentLoading.value = false;
            })
            .catch((error) => {
              console.log("error");
              console.log(error);
              console.log("error");
              showErroeMessage();
              commentLoading.value = false;
            });
          break;
        default:
          commentLoading.value = false;
        // code block
      }
    };

    // comments
    const handleSubmit = () => {
      if (!authLogin() || !commentsValue.value) {
        return;
      }
      //  Comment detectaddCommentsDialog
      commentConfirmLoading.value = true;
      popToxicText.value = "";
      popSentimentText.value = "";
      popHightToxicText.value = "";
      axios
        .post(env.AMDBAPI + "/comments/toxic?title=" + commentsValue.value)
        .then((response) => {
          const commentStatus = response.data.data;
          addCommentsDialog.value = true;
          popToxicText.value =
            "Toxic is " +
            showToxicText(commentStatus.toxic[0]) +
            "(" +
            Number(commentStatus.toxic[0] * 100).toFixed(1) +
            "%)";
          popSentimentText.value =
            "Sentiment is " +
            showSentiemntText(commentStatus.sentiment[0]) +
            "(" +
            Number(commentStatus.sentiment[0] * 100).toFixed(1) +
            "%).";
          commentConfirmLoading.value = false;
          if (commentStatus.toxic[0] > 0.9) {
            popHightToxicText.value =
              "Your comment is SEVERE TOXIC. If you post too much, the administrator will block your account.";
          }
        });
    };

    const confirmAddComment = () => {
      commentLoading.value = true;
      addCommentsDialog.value = false;
      // Add comments
      axios
        .post(
          env.AMDBAPI +
            "comments/addComments?movieId=" +
            movieid.value +
            "&comment=" +
            commentsValue.value +
            "&userId=" +
            currentUser.value.data.userId
        )
        .then((response) => {
          // tmdbreview.value = response.data;
          console.log("Add comments ");
          console.log(response.data);
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

    const fleshMovie = (to, from) => {
      // window.location.reload()
      // if (router.query) {
      //   router.go(0);
      // }
    };

    const showCastDetail = (id) => {
      isShowCastDetail.value = true;
      console.log("showCastDetail");
      console.log(id);
      //Fetch Cast Detials
      axios
        .get(env.tmdbperson + id + "?" + env.tmdbkey + env.tmdbtail)
        .then((response) => {
          castDetail.value = response.data;
          console.log("castDetail detail");
          console.log(castDetail.value);
        });
    };

    //AMDB filter change
    const handleFilterChange = (value) => {
      console.log("handleFilterChange");
      // console.log(value);
      // console.log(ToolMethod.commentsFilter(amdbreview.value, value));
      amdbreview.value = commentsFilter(amdbAllreview.value, value);
    };

    //TMDB filter change
    const handleTMDBFilterChange = (value) => {
      console.log("handleFilterChange2");
      // console.log(data);
      // console.log(value);
      // console.log(ToolMethod.commentsFilter(amdbreview.value, value));
      tmdbreview.value = commentsFilter2(tmdbAllreview.value, value);
    };

    //IMDB filter change
    const handleIMDBFilterChange = (value) => {
      console.log("handleFilterChange2");
      // console.log(data);
      // console.log(value);
      // console.log(ToolMethod.commentsFilter(amdbreview.value, value));
      imdbreview.value = commentsFilter2(imdbAllreview.value, value);
    };

    //Youtube filter change
    const handleYoutubeFilterChange = (value) => {
      console.log("handleFilterChange2");
      // console.log(data);
      // console.log(value);
      // console.log(ToolMethod.commentsFilter(amdbreview.value, value));
      youtubereview.value = commentsFilter2(youtubeAllreview.value, value);
    };

    //Twitter filter change
    const handleTwitterFilterChange = (value) => {
      console.log("handleFilterChange2");
      // console.log(data);
      // console.log(value);
      // console.log(ToolMethod.commentsFilter(amdbreview.value, value));
      twitterreview.value = commentsFilter2(twitterAllreview.value, value);
    };

    const commentsFilter = (value, filter) => {
      console.log("commentsFilter");
      console.log(value);
      let comments = [];
      if (filter === "notoxic") {
        for (let i of value) {
          if (i.toxic < 0.53) {
            comments.push(i);
          }
        }
      } else if (filter === "toxic") {
        for (let i of value) {
          if (i.toxic >= 0.53 && i.toxic < 0.9) {
            comments.push(i);
          }
        }
      } else if (filter === "severetoxic") {
        for (let i of value) {
          if (i.toxic >= 0.9) {
            comments.push(i);
          }
        }
      } else if (filter === "positive") {
        for (let i of value) {
          if (i.sentiment >= 0.5) {
            comments.push(i);
          }
        }
      } else if (filter === "negative") {
        for (let i of value) {
          if (i.sentiment < 0.5) {
            comments.push(i);
          }
        }
      } else {
        comments = value;
      }
      console.log("..............comments");
      console.log(comments);
      return comments;
    };

    const commentsFilter2 = (value, filter) => {
      console.log("commentsFilter");
      console.log(value);
      let comments = [];
      if (filter === "notoxic") {
        for (let i of value) {
          if (i.toxic[0] < 0.53) {
            comments.push(i);
          }
        }
      } else if (filter === "toxic") {
        for (let i of value) {
          if (i.toxic[0] >= 0.53 && i.toxic < 0.9) {
            comments.push(i);
          }
        }
      } else if (filter === "severetoxic") {
        for (let i of value) {
          if (i.toxic[0] >= 0.9) {
            comments.push(i);
          }
        }
      } else if (filter === "positive") {
        for (let i of value) {
          if (i.sentiment[0] >= 0.5) {
            comments.push(i);
          }
        }
      } else if (filter === "negative") {
        for (let i of value) {
          if (i.sentiment[0] < 0.5) {
            comments.push(i);
          }
        }
      } else {
        comments = value;
      }
      console.log("..............comments");
      console.log(comments);
      return comments;
    };

    // Add to like list
    const addLikeList = () => {
      if (!authLogin()) {
        return;
      }
      axios
        .get(
          env.AMDBAPI +
            "member/movieLikes?userId=" +
            currentUser.value.data.userId +
            "&movieId=" +
            movieid.value
        )
        .then((response) => {
          // tmdbreview.value = response.data;
          console.log("Add like list ");
          console.log(response.data);
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
        });
    };

    // Report AMDB comments
    let reportCommentId = "";
    const amdbReport = (item) => {
      if (!authLogin()) {
        return;
      }
      reportCommentId = item.id;
      reportCommentsDialog.value = true;
    };

    const confirmReportComment = () => {
      // Add comments
      axios
        .get(
          env.AMDBAPI +
            "admin/doReport?id=" +
            reportCommentId +
            "&userId=" +
            currentUser.value.data.userId
        )
        .then((response) => {
          // tmdbreview.value = response.data;
          console.log("confirmReportComment ");
          console.log(response.data);
          reportCommentsDialog.value = false;
          if (response.data.code === 200) {
            message.success("Thanks for your report!");
          }
        })
        .catch((error) => {
          reportCommentsDialog.value = false;
          console.log("error");
          console.log(error);
          console.log("error");
          showErroeMessage();
        });
    };

    // Need log in
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
      ellipsis: ref(true),
      judgeBadWord,
      amdbReport,
      handleCancel,
      handleSubmit,
      showCastDetail,
      showToxicText,
      showSentiemntText,
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
      fleshMovie,
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
.product__sidebar__comment__item__text ul {
  padding-left: 0 !important;
}
.anime-details {
  padding-top: 60px;
}

.anime__details__content {
  margin-bottom: 65px;
}

.anime__details__text {
  position: relative;
}

.anime__details__text p {
  color: #b7b7b7;
  font-size: 18px;
  line-height: 30px;
}

.anime__details__pic {
  height: 440px;
  border-radius: 5px;
  position: relative;
}

.anime__details__pic .comment {
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

.anime__details__pic .view {
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

.anime__details__title {
  margin-bottom: 20px;
  padding-right: 100px;
}

.anime__details__title h3 {
  color: #fff;
  font-weight: 700;
  margin-bottom: 13px;
}

.anime__details__title span {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
}

.anime__details__rating {
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

.anime__details__rating span {
  display: block;
  font-size: 18px;
  // color: #b7b7b7;
}

.anime__details__widget {
  margin-bottom: 15px;
}

.anime__details__widget ul {
  margin-bottom: 20px;
}

.anime__details__widget ul li {
  list-style: none;
  font-size: 15px;
  color: #ffffff;
  line-height: 30px;
  position: relative;
  padding-left: 18px;
}

.anime__details__widget ul li:before {
  position: absolute;
  left: 0;
  top: 12px;
  height: 6px;
  width: 6px;
  background: #b7b7b7;
  content: "";
}

.anime__details__widget ul li span {
  color: #b7b7b7;
  width: 115px;
  display: inline-block;
}

.anime__details__btn .follow-btn {
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

.anime__details__btn .watch-btn span {
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

.anime__details__btn .watch-btn i {
  font-size: 20px;
  display: inline-block;
  background: #e53637;
  padding: 11px 5px 16px 8px;
  color: #ffffff;
  border-radius: 0 4px 4px 0;
}

.anime__details__review {
  margin-bottom: 55px;
  .comment-filter {
    .filter-select {
      position: absolute;
      right: 15px;
      top: 70px;
    }
  }
}

.anime__review__item {
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

.anime__review__item__pic {
  float: left;
  margin-right: 20px;
  position: relative;
}

.anime__review__item__pic:before {
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

.anime__review__item__pic img {
  height: 50px;
  width: 50px;
  border-radius: 50%;
}

.anime__review__item__text {
  overflow: hidden;
  background: #494a58;
  padding: 13px 30px 0px 20px;
  border-radius: 10px;

  .comment-text {
    color: #fff;
  }
}

.anime__review__item__text h6 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 10px;
}

.anime__review__item__text h6 span {
  color: #b7b7b7;
  font-weight: 400;
}

.anime__review__item__text p {
  color: #b7b7b7;
  line-height: 23px;
  margin-bottom: 0;
}

.anime__details__form form textarea {
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

.anime__details__form form button {
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

// .pichover {
//   width: 110px;
//   height: 150px;
//   transition: all 0.4s;
//   -moz-transition: all 0.4s;
//   -webkit-transition: all 0.4s;
//   -o-transition: all 0.4s;
//   background-repeat: no-repeat;
//   background-position: center;
//   background-size: 100% 100%;
// }

// .pichover:hover {
//   object-fit: cover;
//   background-size: 110% 110%;
//   -webkit-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
//   -moz-box-shadow: 2px 12px 10px rgba(138, 138, 138, 0.603);
//   box-shadow: 12px 12px 10px rgba(138, 138, 138, 0.603);
//   cursor: pointer;
// }

@media only screen and (max-width: 800px) {
  .filter-select {
    position: initial !important;
    margin-top: 30px;
  }
}
</style>