# JLPT N4 Vocabulary (Goi)

Source-of-truth catalogue. Build pipeline parses into `data/vocab.json`. Schema per spec.

Entry format:
```
- <form> (<reading>) - [<pos>] <gloss> [tier:<tier>] [examples:<count>]
```

PoS tags: `[n.]`, `[v1]`, `[v2]`, `[v3]`, `[i-adj]`, `[na-adj]`, `[adv.]`, `[part.]`, `[conj.]`, `[pron.]`, `[count.]`, `[num.]`, `[dem.]`, `[Q-word]`, `[exp.]`, `[interj.]`.

**Tag the WORD's actual PoS, not the section default** (anti-pattern AP-1).

Corpus = N5 prerequisite (1041 entries, inherited verbatim) + N4 seed (~100+ entries from a-h sample).
Full ~600-entry N4 corpus to be added in subsequent passes from Tanos N4 CSV.

---

## N5 prerequisite vocabulary (inherited)

All N5 vocabulary is a hard prerequisite. The list below is the verbatim N5 catalogue, included so X-6.6 (Group-1 ru-verb exception flags) and JA-31 (PoS parity) pass on the unified N4 vocab.


Exhaustive list of JLPT N5 vocabulary, grouped for readability. Each entry follows the format:

`Japanese (Reading) - English meaning`

## Kanji Usage Rule

To match the N5 learner's actual reading ability, this list uses **only kanji that appear in the N5 kanji syllabus** (see `kanji_n5.md`).

- If every kanji in a word is part of the N5 syllabus, the kanji form is shown (e.g., 学生).
- If a word contains any kanji that is *not* in the N5 syllabus, the entire word is rendered in **hiragana** (or katakana for loanwords) - even if part of the word would otherwise use a known kanji. This avoids "half-known" presentations.
- Loanwords stay in their conventional katakana form.

## Tier Legend

- Items without a tag are **Core N5** - confidently expected at N5.
- **[Ext]** = *Extended / borderline* - listed by some N5 sources but commonly placed at N4 by others. Useful for recognition; do not over-prioritize.
- **[Cul]** = *Cultural / situational* - encountered in everyday Japan but rarely a focus on the N5 exam.

## Part-of-Speech Tags

Each entry carries a bracketed PoS tag in the gloss column for fast scanning. Mirrors the `pos` field in `data/vocab.json`. Verb classes use Japanese-grammar conventions, not English categories.

- **[n.]** = noun
- **[v1]** = godan verb (Group 1, consonant-stem)
- **[v2]** = ichidan verb (Group 2, vowel-stem)
- **[v3]** = irregular verb (する / 来る only at N5)
- **[i-adj]** = i-adjective
- **[na-adj]** = na-adjective
- **[adv.]** = adverb
- **[part.]** = particle
- **[conj.]** = conjunction
- **[pron.]** = pronoun
- **[count.]** = counter
- **[num.]** = numeral
- **[dem.]** = demonstrative (こ/そ/あ/ど series)
- **[Q-word]** = interrogative (なに / どこ / etc.)
- **[exp.]** = fixed expression / phrase
- **[interj.]** = interjection

## Variant Policy

When two forms exist (e.g., a Sino-Japanese term plus a katakana loan), the dominant form is listed first, with the alternate noted on the same line. Some words intentionally appear under more than one section (e.g., 名前 under both *Common Nouns* and *Misc Useful Items*) because they belong functionally to multiple thematic groups. This is by design, not duplication.

---

## 1. People - Pronouns and Self

- 私 (わたし) - [pron.] I, me
- 私たち (わたしたち) - [pron.] we
- あなた - [pron.] you
- かれ - [pron.] boyfriend; he, him (the third-person sense is somewhat literary; spoken Japanese normally drops the pronoun)
- かのじょ - [pron.] girlfriend; she, her (the third-person sense is somewhat literary; spoken Japanese normally drops the pronoun)
- かた - [n.] person (polite)
- 人 (ひと) - [n.] person
- みなさん - [n.] everyone (polite)
- だれ - [Q-word] who
- どなた - [Q-word] who (polite)
- じぶん - [pron.] oneself

## 2. People - Family

- かぞく - [n.] family
- 父 (ちち) - [n.] father (own)
- 母 (はは) - [n.] mother (own)
- お父さん (おとうさん) - [n.] father (someone else's / address form)
- お母さん (おかあさん) - [n.] mother (someone else's / address form)
- あに - [n.] older brother (own)
- あね - [n.] older sister (own)
- おとうと - [n.] younger brother
- いもうと - [n.] younger sister
- おにいさん - [n.] older brother (polite)
- おねえさん - [n.] older sister (polite)
- きょうだい - [n.] siblings
- りょうしん - [n.] parents
- そふ - [n.] grandfather (own)
- そぼ - [n.] grandmother (own)
- おじいさん - [n.] grandfather, elderly man
- おばあさん - [n.] grandmother, elderly woman
- おじさん - [n.] uncle, middle-aged man
- おばさん - [n.] aunt, middle-aged woman
- 子ども (こども) - [n.] child (often written こども in everyday text)
- 男の子 (おとこのこ) - [n.] boy
- 女の子 (おんなのこ) - [n.] girl
- 男 (おとこ) - [n.] man
- 女 (おんな) - [n.] woman
- 大人 (おとな) - [n.] adult
- ともだち - [n.] friend

## 3. People - Roles

- 学生 (がくせい) - [n.] student
- せいと - [n.] pupil, schoolchild
- 先生 (せんせい) - [n.] teacher, doctor
- いしゃ - [n.] doctor
- 会社員 (かいしゃいん) - [n.] company employee
- 駅員 (えきいん) - [n.] station staff
- 店員 (てんいん) - [n.] shop clerk
- けいかん - [n.] police officer **[Ext]**
- おまわりさん - [n.] police officer (friendly) **[Ext]**
- りゅうがくせい - [n.] international student **[Ext]**
- 外国人 (がいこくじん) - [n.] foreigner

## 4. Body Parts

- からだ - [n.] body
- あたま - [n.] head
- かお - [n.] face
- め - [n.] eye
- みみ - [n.] ear
- はな - [n.] nose
- くち - [n.] mouth
- は - [n.] tooth
- て - [n.] hand
- あし - [n.] leg, foot
- おなか - [n.] stomach, belly
- せ - [n.] back, height

## 5. Demonstratives (こそあど)

- これ - [dem.] this (thing near speaker)
- それ - [dem.] that (thing near listener)
- あれ - [dem.] that (over there)
- どれ - [dem.] which (one)
- この - [dem.] this (modifier)
- その - [dem.] that (modifier)
- あの - [dem.] that over there (modifier)
- どの - [dem.] which (modifier)
- ここ - [dem.] here
- そこ - [dem.] there
- あそこ - [dem.] over there
- どこ - [dem.] where
- こちら - [dem.] this way / this person (polite)
- そちら - [dem.] that way
- あちら - [dem.] that way (over there)
- どちら - [dem.] which way
- こっち - [dem.] this way (casual)
- そっち - [dem.] that way (casual)
- あっち - [dem.] that way over there (casual)
- どっち - [dem.] which way (casual)
- こんな - [dem.] this kind of
- そんな - [dem.] that kind of
- あんな - [dem.] that kind of (over there)
- どんな - [dem.] what kind of
- こう - [dem.] like this
- そう - [dem.] like that
- ああ - [dem.] like that (over there)
- どう - [dem.] how

## 6. Question Words

- 何 (なに / なん) - [Q-word] what
- いつ - [Q-word] when
- いくら - [Q-word] how much (price)
- いくつ - [Q-word] how many, how old
- 何時 (なんじ) - [Q-word] what time
- 何曜日 (なんようび) - [Q-word] what day of the week
- 何月 (なんがつ) - [Q-word] what month
- 何日 (なんにち) - [Q-word] what day
- なぜ - [Q-word] why
- どうして - [Q-word] why
- 何で (なんで) - [Q-word] why, by what means

## 7. Numbers

- ゼロ / れい - [num.] zero
- 一 (いち) - [num.] one
- 二 (に) - [num.] two
- 三 (さん) - [num.] three
- 四 (し / よん) - [num.] four
- 五 (ご) - [num.] five
- 六 (ろく) - [num.] six
- 七 (しち / なな) - [num.] seven
- 八 (はち) - [num.] eight
- 九 (きゅう / く) - [num.] nine
- 十 (じゅう) - [num.] ten
- 十一 (じゅういち) - [num.] eleven
- 二十 (にじゅう) - [num.] twenty
- 百 (ひゃく) - [num.] hundred
- 千 (せん) - [num.] thousand
- 万 (まん) - [num.] ten thousand
- 一万 (いちまん) - [num.] ten thousand
- おく - [num.] hundred million **[Ext]**

## 8. Native Counters (つ-series)

- 一つ (ひとつ) - [count.] one (thing)
- 二つ (ふたつ) - [count.] two
- 三つ (みっつ) - [count.] three
- 四つ (よっつ) - [count.] four
- 五つ (いつつ) - [count.] five
- 六つ (むっつ) - [count.] six
- 七つ (ななつ) - [count.] seven
- 八つ (やっつ) - [count.] eight
- 九つ (ここのつ) - [count.] nine
- 十 (とお) - [count.] ten
- いくつ - [count.] how many

## 9. Counters (Common)

- 人 (にん) - [count.] counter for people
- 一人 (ひとり) - [count.] one person
- 二人 (ふたり) - [count.] two people
- まい - [count.] counter for flat objects
- 本 (ほん) - [count.] counter for long thin objects
- だい - [count.] counter for machines / vehicles
- さつ - [count.] counter for books
- ひき - [count.] counter for small animals
- はい - [count.] counter for cups / glasses
- こ - [count.] counter for small objects
- かい - [count.] floor of a building (e.g., 3-かい = 3rd floor)
- かい - [count.] number of times / occurrences (e.g., 3-かい = three times). Same kana, different counter (different kanji); context disambiguates.
- 番 (ばん) - [count.] number, ordinal
- ど - [count.] degrees, occurrences

## 10. Time - General

- とき - [n.] time, when
- 時間 (じかん) - [n.] time, hour
- とけい - [n.] clock, watch
- 今 (いま) - [n.] now
- 今日 (きょう) - [n.] today
- あした - [n.] tomorrow
- きのう - [n.] yesterday
- あさって - [n.] day after tomorrow
- おととい - [n.] day before yesterday
- あさ - [n.] morning
- ひる - [n.] noon, daytime
- ゆうがた - [n.] evening
- よる - [n.] night
- ばん - [n.] evening, night
- けさ - [n.] this morning
- こんばん - [n.] this evening
- こんや - [n.] tonight
- 午前 (ごぜん) - [n.] A.M.
- 午後 (ごご) - [n.] P.M.
- 半 (はん) - [n.] half (past)
- 分 (ふん / ぷん) - [n.] minute(s)
- びょう - [n.] second(s)

## 11. Time - Days, Weeks, Months, Years

- 日 (ひ) - [n.] day
- 一日 (ついたち) - [n.] 1st of the month
- 一日 (いちにち) - [n.] one day, a whole day (note: same kanji 一日 with a different reading, distinct from ついたち; context disambiguates)
- 二日 (ふつか) - [n.] 2nd / two days
- 三日 (みっか) - [n.] 3rd / three days
- 四日 (よっか) - [n.] 4th / four days
- 五日 (いつか) - [n.] 5th / five days
- 六日 (むいか) - [n.] 6th / six days
- 七日 (なのか) - [n.] 7th / seven days
- 八日 (ようか) - [n.] 8th / eight days
- 九日 (ここのか) - [n.] 9th / nine days
- 十日 (とおか) - [n.] 10th / ten days
- 二十日 (はつか) - [n.] 20th / twenty days
- 週 (しゅう) - [n.] week
- 先週 (せんしゅう) - [n.] last week
- 今週 (こんしゅう) - [n.] this week
- 来週 (らいしゅう) - [n.] next week
- 毎週 (まいしゅう) - [n.] every week
- 月曜日 (げつようび) - [n.] Monday
- 火曜日 (かようび) - [n.] Tuesday
- 水曜日 (すいようび) - [n.] Wednesday
- 木曜日 (もくようび) - [n.] Thursday
- 金曜日 (きんようび) - [n.] Friday
- 土曜日 (どようび) - [n.] Saturday
- 日曜日 (にちようび) - [n.] Sunday
- しゅうまつ - [n.] weekend
- 月 (つき) - [n.] month, moon
- 一月 (いちがつ) - [n.] January
- 二月 (にがつ) - [n.] February
- 三月 (さんがつ) - [n.] March
- 四月 (しがつ) - [n.] April
- 五月 (ごがつ) - [n.] May
- 六月 (ろくがつ) - [n.] June
- 七月 (しちがつ) - [n.] July
- 八月 (はちがつ) - [n.] August
- 九月 (くがつ) - [n.] September
- 十月 (じゅうがつ) - [n.] October
- 十一月 (じゅういちがつ) - [n.] November
- 十二月 (じゅうにがつ) - [n.] December
- 先月 (せんげつ) - [n.] last month
- 今月 (こんげつ) - [n.] this month
- 来月 (らいげつ) - [n.] next month
- 毎月 (まいつき) - [n.] every month
- 年 (とし / ねん) - [n.] year
- きょねん - [n.] last year
- 今年 (ことし) - [n.] this year
- 来年 (らいねん) - [n.] next year
- 毎年 (まいとし / まいねん) - [n.] every year (まいとし is more common in conversation; まいねん in formal/written contexts)
- おととし - [n.] year before last
- さらいねん - [n.] year after next **[Ext]**
- たんじょうび - [n.] birthday

## 12. Time - Frequency / Sequence

- 毎日 (まいにち) - [n.] every day
- まいあさ - [n.] every morning
- まいばん - [n.] every night
- いつも - [adv.] always
- よく - [adv.] often
- 時々 (ときどき) - [adv.] sometimes
- たまに - [adv.] occasionally
- あまり - [adv.] not very (with negative)
- ぜんぜん - [adv.] not at all (with negative)
- すぐ - [adv.] soon, immediately
- もう - [adv.] already (with affirmative); anymore (with negative); more (as in もう一つ)
- もうすぐ - [adv.] soon, before long
- まだ - [adv.] still, not yet
- はじめて - [adv.] for the first time
- さいしょ - [n.] first, beginning
- さいご - [n.] last, end
- つぎ - [n.] next
- 後で (あとで) - [n.] later
- 前 (まえ) - [n.] before, in front
- 後 (あと) / うしろ - [n.] after, behind

## 13. Locations and Places (general)

- ところ - [n.] place
- いえ / うち - [n.] house, home
- へや - [n.] room
- だいどころ - [n.] kitchen
- おてあらい - [n.] restroom
- トイレ - [n.] toilet
- おふろ - [n.] bath
- げんかん - [n.] entrance
- にわ - [n.] garden
- 学校 (がっこう) - [n.] school
- 大学 (だいがく) - [n.] university
- 高校 (こうこう) - [n.] high school
- きょうしつ - [n.] classroom
- としょかん - [n.] library
- びょういん - [n.] hospital
- ぎんこう - [n.] bank
- ゆうびんきょく - [n.] post office
- 会社 (かいしゃ) - [n.] company
- じむしょ - [n.] office
- お店 (おみせ) - [n.] shop
- スーパー - [n.] supermarket
- デパート - [n.] department store
- きっさてん - [n.] café
- レストラン - [n.] restaurant
- やおや - [n.] greengrocer
- ほんや - [n.] bookstore
- はなや - [n.] flower shop
- にくや - [n.] butcher
- パンや - [n.] bakery
- 駅 (えき) - [n.] station
- くうこう - [n.] airport
- こうえん - [n.] park
- どうぶつえん - [n.] zoo **[Ext]**
- びじゅつかん - [n.] art museum **[Ext]**
- えいがかん - [n.] movie theater
- ホテル - [n.] hotel
- りょかん - [n.] Japanese inn **[Cul]**
- たいしかん - [n.] embassy **[Ext]**
- こうばん - [n.] police box **[Cul]**
- こうじょう - [n.] factory
- こうさてん - [n.] intersection
- いりぐち - [n.] entrance, entry
- しょくどう - [n.] cafeteria, dining room
- たてもの - [n.] building
- ろうか - [n.] hallway, corridor
- プール - [n.] swimming pool
- ポスト - [n.] post (mailbox)
- 道 (みち) - [n.] road, way
- とおり - [n.] street
- かど - [n.] corner
- はし - [n.] bridge
- まち - [n.] town
- むら - [n.] village
- 国 (くに) - [n.] country
- 外 (そと) - [n.] outside
- 中 (なか) - [n.] inside, middle
- 上 (うえ) - [n.] top, above
- 下 (した) - [n.] under, below
- 前 (まえ) - [n.] front
- 後ろ (うしろ) - [n.] back, behind
- 左 (ひだり) - [n.] left
- 右 (みぎ) - [n.] right
- となり - [n.] next to
- よこ - [n.] side
- ちかく - [n.] near
- とおく - [n.] far
- むこう - [n.] over there, beyond
- 北 (きた) - [n.] north
- 南 (みなみ) - [n.] south
- 東 (ひがし) - [n.] east
- 西 (にし) - [n.] west

## 14. Nature and Weather

- 山 (やま) - [n.] mountain
- 川 (かわ) - [n.] river
- うみ - [n.] sea, ocean
- いけ - [n.] pond
- みずうみ - [n.] lake
- もり - [n.] forest
- 木 (き) - [n.] tree
- 花 (はな) - [n.] flower
- くさ - [n.] grass
- は - [n.] leaf
- いし - [n.] stone
- 田 (た) - [n.] rice field
- 空 (そら) - [n.] sky
- くも - [n.] cloud
- たいよう - [n.] sun
- 月 (つき) - [n.] moon
- ほし - [n.] star
- 雨 (あめ) - [n.] rain
- ゆき - [n.] snow
- かぜ - [n.] wind
- 天気 (てんき) - [n.] weather
- はれ - [n.] clear weather
- くもり - [n.] cloudy
- はる - [n.] spring
- なつ - [n.] summer
- あき - [n.] autumn
- ふゆ - [n.] winter
- あつい - [i-adj] hot (weather)
- さむい - [i-adj] cold (weather)
- すずしい - [i-adj] cool
- あたたかい - [i-adj] warm
- 火 (ひ) - [n.] fire
- 水 (みず) - [n.] water (cold)
- おゆ - [n.] hot water

## 15. Animals

- どうぶつ - [n.] animal
- いぬ - [n.] dog
- ねこ - [n.] cat
- とり - [n.] bird
- さかな - [n.] fish
- うま - [n.] horse
- うし - [n.] cow
- ぶた - [n.] pig
- にわとり - [n.] chicken
- ぞう - [n.] elephant **[Cul]**
- むし - [n.] insect

## 16. Food and Drink - General

- たべもの - [n.] food
- のみもの - [n.] drink
- あさごはん - [n.] breakfast
- ひるごはん - [n.] lunch
- ばんごはん - [n.] dinner
- ゆうはん - [n.] dinner (alternate)
- ごはん - [n.] rice, meal
- しょくじ - [n.] meal
- おべんとう - [n.] boxed lunch
- おかし - [n.] sweets, snacks

## 17. Food - Items

- パン - [n.] bread
- たまご - [n.] egg
- にく - [n.] meat
- ぎゅうにく - [n.] beef
- ぶたにく - [n.] pork
- とりにく - [n.] chicken (meat)
- さかな - [n.] fish
- やさい - [n.] vegetable
- くだもの - [n.] fruit
- りんご - [n.] apple
- みかん - [n.] mandarin orange
- バナナ - [n.] banana
- いちご - [n.] strawberry
- ぶどう - [n.] grape
- すいか - [n.] watermelon
- レモン - [n.] lemon
- だいこん - [n.] daikon radish **[Cul]**
- にんじん - [n.] carrot
- たまねぎ - [n.] onion
- じゃがいも - [n.] potato
- トマト - [n.] tomato
- きゅうり - [n.] cucumber
- キャベツ - [n.] cabbage
- こめ - [n.] uncooked rice
- しお - [n.] salt
- さとう - [n.] sugar
- しょうゆ - [n.] soy sauce **[Cul]**
- みそ - [n.] miso **[Cul]**
- バター - [n.] butter
- チーズ - [n.] cheese
- すし - [n.] sushi **[Cul]**
- 天ぷら (てんぷら) - [n.] tempura **[Cul]**
- カレー - [n.] curry
- ラーメン - [n.] ramen
- うどん - [n.] udon **[Cul]**
- そば - [n.] soba **[Cul]**
- ハンバーガー - [n.] hamburger
- サンドイッチ - [n.] sandwich
- サラダ - [n.] salad
- スープ - [n.] soup
- ケーキ - [n.] cake
- アイスクリーム - [n.] ice cream
- チョコレート - [n.] chocolate
- あめ - [n.] candy (homophone of 雨 "rain")

## 18. Drinks

- 水 (みず) - [n.] water
- おゆ - [n.] hot water
- おちゃ - [n.] tea, green tea (Japanese tea)
- こうちゃ - [n.] black tea
- コーヒー - [n.] coffee
- ぎゅうにゅう - [n.] milk (also commonly: ミルク)
- ジュース - [n.] juice
- おさけ - [n.] alcohol, sake
- ビール - [n.] beer
- ワイン - [n.] wine

## 19. Tableware and Cooking

- さら - [n.] plate
- おさら - [n.] plate (polite)
- ちゃわん - [n.] rice bowl
- おわん - [n.] bowl
- はし - [n.] chopsticks
- スプーン - [n.] spoon
- フォーク - [n.] fork
- ナイフ - [n.] knife
- コップ - [n.] cup, glass
- カップ - [n.] cup (alt of コップ)
- れいぞうこ - [n.] refrigerator
- なべ - [n.] pot, pan

## 20. Colors

- いろ - [n.] color
- 白 (しろ) - [n.] white (noun)
- 白い (しろい) - [i-adj] white (adj)
- くろ - [n.] black (noun)
- くろい - [i-adj] black (adj)
- あか - [n.] red (noun)
- あかい - [i-adj] red (adj)
- あお - [n.] blue (noun)
- あおい - [i-adj] blue (adj)
- きいろ - [n.] yellow (noun)
- きいろい - [i-adj] yellow (adj)
- ちゃいろ - [n.] brown
- みどり - [n.] green
- ピンク - [n.] pink

## 21. Clothing and Accessories

- ふく - [n.] clothes
- ようふく - [n.] Western clothes
- きもの - [n.] kimono, traditional clothes **[Cul]**
- うわぎ - [n.] jacket, coat
- コート - [n.] coat
- セーター - [n.] sweater
- シャツ - [n.] shirt
- Tシャツ (ティーシャツ) - [n.] T-shirt
- ワイシャツ - [n.] dress shirt
- ズボン - [n.] trousers
- スカート - [n.] skirt
- ネクタイ - [n.] necktie
- ぼうし - [n.] hat, cap
- くつ - [n.] shoes
- くつした - [n.] socks
- ハンカチ - [n.] handkerchief
- かばん - [n.] bag
- さいふ - [n.] wallet
- めがね - [n.] glasses
- とけい - [n.] watch, clock
- ボタン - [n.] button
- ポケット - [n.] pocket
- かさ - [n.] umbrella

## 22. Money and Shopping

- お金 (おかね) - [n.] money
- 円 (えん) - [n.] yen
- ドル - [n.] dollar
- ねだん - [n.] price
- きっぷ - [n.] ticket
- きって - [n.] postage stamp
- はがき - [n.] postcard
- ふうとう - [n.] envelope
- てがみ - [n.] letter
- にもつ - [n.] luggage, package
- おみやげ - [n.] souvenir **[Cul]**
- レジ - [n.] register, cashier

## 23. Transport

- 車 (くるま) - [n.] car
- じどうしゃ - [n.] automobile
- じてんしゃ - [n.] bicycle
- バイク - [n.] motorbike
- バス - [n.] bus
- タクシー - [n.] taxi
- 電車 (でんしゃ) - [n.] train (electric)
- きしゃ - [n.] train (steam, archaic but still in older N5 lists) **[Ext]**
- ちかてつ - [n.] subway
- ひこうき - [n.] airplane
- ふね - [n.] ship, boat
- 道 (みち) - [n.] road
- しんごう - [n.] traffic light, signal

## 24. School and Study

- べんきょう - [n.] study
- じゅぎょう - [n.] class, lesson
- しゅくだい - [n.] homework
- しけん - [n.] exam
- テスト - [n.] test
- しつもん - [n.] question
- こたえ - [n.] answer
- いみ - [n.] meaning
- ことば - [n.] word, language
- じ - [n.] character (writing), letter (of an alphabet)
- かんじ - [n.] kanji, Chinese characters
- かな - [n.] kana
- ひらがな - [n.] hiragana
- カタカナ - [n.] katakana
- もじ - [n.] letter, character
- ぶん - [n.] sentence
- ぶんしょう - [n.] composition, text
- ぶんぽう - [n.] grammar
- れい - [n.] example
- れんしゅう - [n.] practice
- 本 (ほん) - [n.] book
- きょうかしょ - [n.] textbook
- じしょ - [n.] dictionary
- ざっし - [n.] magazine
- 新聞 (しんぶん) - [n.] newspaper
- かみ - [n.] paper
- えんぴつ - [n.] pencil
- ボールペン - [n.] ballpoint pen
- まんねんひつ - [n.] fountain pen **[Ext]**
- ペン - [n.] pen
- ノート - [n.] notebook
- こくばん - [n.] blackboard
- チョーク - [n.] chalk
- つくえ - [n.] desk
- いす - [n.] chair
- けしゴム - [n.] eraser
- ちず - [n.] map
- しゃしん - [n.] photograph
- え - [n.] picture, drawing
- 番号 (ばんごう) - [n.] number
- 電気 (でんき) - [n.] electricity, light
- 電話 (でんわ) - [n.] telephone
- 電話番号 (でんわばんごう) - [n.] phone number

## 25. Languages and Countries

- 日本 (にほん / にっぽん) - [n.] Japan
- 日本語 (にほんご) - [n.] Japanese (language)
- 日本人 (にほんじん) - [n.] Japanese (person)
- アメリカ - [n.] America
- えいご - [n.] English (language)
- 中国 (ちゅうごく) - [n.] China
- 中国語 (ちゅうごくご) - [n.] Chinese (language)
- かんこく - [n.] Korea
- かんこくご - [n.] Korean (language)
- フランス - [n.] France
- フランスご - [n.] French (language)
- ドイツ - [n.] Germany
- スペイン - [n.] Spain
- イギリス - [n.] United Kingdom
- 外国 (がいこく) - [n.] foreign country
- 外国語 (がいこくご) - [n.] foreign language

## 26. House and Furniture

- いえ / うち - [n.] house, home
- アパート - [n.] apartment
- マンション - [n.] condominium **[Cul]**
- ドア - [n.] door
- と - [n.] door (Japanese-style)
- もん - [n.] gate
- まど - [n.] window
- かべ - [n.] wall
- かいだん - [n.] stairs
- エレベーター - [n.] elevator
- へや - [n.] room
- げんかん - [n.] entrance
- いま - [n.] living room
- しんしつ - [n.] bedroom
- ベッド - [n.] bed
- ふとん - [n.] futon **[Cul]**
- もうふ - [n.] blanket
- まくら - [n.] pillow
- テーブル - [n.] table
- つくえ - [n.] desk
- いす - [n.] chair
- たな - [n.] shelf
- ほんだな - [n.] bookshelf
- カーテン - [n.] curtain
- かぎ - [n.] key, lock
- 電気 (でんき) - [n.] light
- せっけん - [n.] soap
- はブラシ - [n.] toothbrush
- タオル - [n.] towel
- テープ - [n.] tape
- テレビ - [n.] TV
- ラジオ - [n.] radio
- カメラ - [n.] camera
- ビデオ - [n.] video
- えいが - [n.] movie
- おんがく - [n.] music
- うた - [n.] song
- え - [n.] picture
- ピアノ - [n.] piano
- ギター - [n.] guitar

## 27. Verbs - Group 1 (う-verbs)

> **Group-1 ru-verb exceptions:** 入る, 帰る, 走る, 知る, 切る, and 要る look like Group 2 verbs (they end in -iる or -eる) but are actually Group 1. They are the standard "Group-1 ru-verb" exceptions tested at N5 and are flagged in this list. Memorize these six.

- 会う (あう) - [v1] to meet
- 言う (いう) - [v1] to say
- 行く (いく) - [v1] to go
- うたう - [v1] to sing
- おもう - [v1] to think
- 買う (かう) - [v1] to buy
- 書く (かく) - [v1] to write
- 聞く (きく) - [v1] to listen, to ask
- きる - [v1] to cut (Group 1 exception - looks like Group 2)
- つくる - [v1] to make
- しる - [v1] to know (Group 1 exception - looks like Group 2)
- すむ - [v1] to live (reside)
- 立つ (たつ) - [v1] to stand
- とる - [v1] to take, to pick up (general)
- とる - [v1] to take (a photo or video) - homophone of the above; uses a different kanji (not in N5 syllabus); semantically a specialization of "take"
- なく - [v1] to cry (animals)
- 飲む (のむ) - [v1] to drink
- 入る (はいる) - [v1] to enter (Group 1 exception - looks like Group 2)
- はく - [v1] to put on (lower body)
- 話す (はなす) - [v1] to speak
- はしる - [v1] to run (Group 1 exception - looks like Group 2)
- はたらく - [v1] to work
- まつ - [v1] to wait
- もつ - [v1] to hold, to have
- 休む (やすむ) - [v1] to rest
- 読む (よむ) - [v1] to read
- わたる - [v1] to cross
- 分かる (わかる) - [v1] to understand
- おわる - [v1] to end
- はじまる - [v1] to begin (intransitive)
- かえる - [v1] to return home (Group 1 exception - looks like Group 2)
- うる - [v1] to sell
- おす - [v1] to push
- およぐ - [v1] to swim
- ひく - [v1] to play (a string instrument like guitar/piano)
- ひく - [v1] to pull (homophone of the above; separate verb, separate kanji - both are common N5 readings of ひく)
- よぶ - [v1] to call
- とぶ - [v1] to fly, to jump
- こまる - [v1] to be troubled **[Ext]**
- ならぶ - [v1] to line up **[Ext]**
- のぼる - [v1] to climb **[Ext]**
- わたす - [v1] to hand over **[Ext]**
- ぬぐ - [v1] to take off (clothes)
- あらう - [v1] to wash
- いそぐ - [v1] to hurry
- しぬ - [v1] to die
- すう - [v1] to breathe in, to smoke
- ちがう - [v1] to differ
- つかう - [v1] to use
- つく - [v1] to arrive
- ならう - [v1] to learn
- はる - [v1] to stick, to paste
- まがる - [v1] to turn
- みがく - [v1] to polish, to brush **[Ext]**
- もっていく - [v1] to take (something)
- もってくる - [v1] to bring (something)
- あく - [v1] to open (intransitive; pair with あける)
- しまる - [v1] to close (intransitive; pair with しめる)
- だす - [v1] to take out, to put out (transitive; pair with でる)
- おとす - [v1] to drop (transitive; pair with おちる)
- ふく - [v1] to blow (of the wind)
- ふる - [v1] to fall (rain, snow)
- くもる - [v1] to become cloudy
- なくす - [v1] to lose (something)
- のる - [v1] to get on (train, bus, plane)
- すわる - [v1] to sit
- たのむ - [v1] to ask (a favor)
- とまる - [v1] to stop (intransitive)
- おく - [v1] to place, to put
- さく - [v1] to bloom
- かかる - [v1] to take (time / money)
- さす - [v1] to put up (an umbrella), to raise
- けす - [v1] to turn off, to erase (godan / Group 1; conjugates けします, けして)

## 28. Verbs - Group 2 (る-verbs)

- いる - [v2] to exist (animate)
- 食べる (たべる) - [v2] to eat
- 見る (みる) - [v2] to see, to watch
- ねる - [v2] to sleep
- おきる - [v2] to get up
- 出る (でる) - [v2] to leave, to go out
- 入れる (いれる) - [v2] to put in
- あける - [v2] to open (transitive)
- しめる - [v2] to close (transitive)
- おしえる - [v2] to teach
- おぼえる - [v2] to remember
- わすれる - [v2] to forget
- かりる - [v2] to borrow
- こたえる - [v2] to answer
- 出かける (でかける) - [v2] to go out
- かける - [v2] to call (phone), to wear (glasses)
- きる - [v2] to wear (upper body)
- つける - [v2] to switch on
- ならべる - [v2] to line up (transitive) **[Ext]**
- はじめる - [v2] to begin (transitive)
- 見せる (みせる) - [v2] to show
- あびる - [v2] to bathe (shower)
- いれる - [v2] to make (tea / coffee) (note: same form as 入れる; context distinguishes)
- あつめる - [v2] to collect
- きえる - [v2] to go off, to disappear (intransitive; pair with けす)
- おちる - [v2] to fall (intransitive; pair with おとす)
- はれる - [v2] to be sunny / clear up
- つかれる - [v2] to get tired
- 生まれる (うまれる) - [v2] to be born
- おりる - [v2] to get off (train, bus)
- しめる - [v2] to tie / fasten / tighten (distinct from しめる "to close")
- つとめる - [v2] to work for / be employed (ichidan / Group 2; conjugates つとめます, つとめて)

## 29. Verbs - Irregular and する-verbs

- する - [v3] to do
- 来る (くる) - [v3] to come
- べんきょうする - [v3] to study
- けっこんする - [v3] to get married
- さんぽする - [v3] to take a walk
- りょこうする - [v3] to travel
- れんしゅうする - [v3] to practice
- しつもんする - [v3] to ask a question
- しごとする - [v3] to work
- 電話する (でんわする) - [v3] to telephone
- コピーする - [v3] to copy
- そうじする - [v3] to clean
- せんたくする - [v3] to do laundry
- かいものする - [v3] to go shopping

## 30. Verbs - Existence and Possession

- ある - [v1] to exist (inanimate)
- いる - [v2] to exist (animate) (also in §28 - listed here for thematic completeness with other existence/possession verbs)
- いる - [v1] to need (Group 1 exception - looks like Group 2; homophone of existence-いる which is Group 2)
- ござる / ございます - [v1] to be (very polite)
- やる - [v1] to give (down / casual)
- あげる - [v2] to give
- もらう - [v1] to receive
- くれる - [v2] to give (to me / us)
- かす - [v1] to lend
- かりる - [v2] to borrow
- かえす - [v1] to return (something)

## 31. い-Adjectives

- 大きい (おおきい) - [i-adj] big
- 小さい (ちいさい) - [i-adj] small
- 新しい (あたらしい) - [i-adj] new
- 古い (ふるい) - [i-adj] old (not for people)
- いい / よい - [i-adj] good
- わるい - [i-adj] bad
- あつい - [i-adj] hot (weather; separate adjective from the two below despite shared reading)
- さむい - [i-adj] cold (weather)
- あつい - [i-adj] hot (to the touch; separate adjective and separate kanji - homophone of the hot-weather one)
- つめたい - [i-adj] cold (to touch)
- 高い (たかい) - [i-adj] high, tall, expensive
- ひくい - [i-adj] low, short (height)
- 安い (やすい) - [i-adj] cheap
- 長い (ながい) - [i-adj] long
- みじかい - [i-adj] short (length)
- ひろい - [i-adj] wide, spacious
- せまい - [i-adj] narrow
- おもい - [i-adj] heavy
- かるい - [i-adj] light (weight)
- あつい - [i-adj] thick (e.g., a thick book; separate adjective and separate kanji - third homophone of the あつい readings above)
- うすい - [i-adj] thin
- ふとい - [i-adj] thick (round things)
- ほそい - [i-adj] thin (round things)
- つよい - [i-adj] strong
- よわい - [i-adj] weak
- はやい - [i-adj] early (time-related) - and separately, はやい - fast (speed-related). Two separate adjectives sharing the kana reading; the kanji disambiguates.
- おそい - [i-adj] slow, late
- たのしい - [i-adj] fun, enjoyable
- うれしい - [i-adj] happy
- かなしい - [i-adj] sad
- さびしい - [i-adj] lonely
- いたい - [i-adj] painful
- かわいい - [i-adj] cute
- うつくしい - [i-adj] beautiful
- きたない - [i-adj] dirty
- いそがしい - [i-adj] busy
- やさしい - [i-adj] easy (of a task) - and separately, やさしい - kind / gentle (of a person). Two separate adjectives sharing the kana reading; different kanji distinguish them.
- むずかしい - [i-adj] difficult
- おもしろい - [i-adj] interesting, funny
- つまらない - [i-adj] boring
- おいしい - [i-adj] delicious
- まずい - [i-adj] tastes bad
- あまい - [i-adj] sweet
- からい - [i-adj] spicy, salty
- にがい - [i-adj] bitter
- おおい - [i-adj] many
- すくない - [i-adj] few
- ちかい - [i-adj] near
- とおい - [i-adj] far
- あかるい - [i-adj] bright
- くらい - [i-adj] dark
- あたたかい - [i-adj] warm
- すずしい - [i-adj] cool
- まるい - [i-adj] round
- しかくい - [i-adj] square
- わかい - [i-adj] young
- きいろい - [i-adj] yellow
- あおい - [i-adj] blue
- あかい - [i-adj] red
- くろい - [i-adj] black
- 白い (しろい) - [i-adj] white
- ちゃいろい - [i-adj] brown
- あぶない - [i-adj] dangerous
- ほしい - [i-adj] want (something)
- ぬるい - [i-adj] lukewarm
- うるさい - [i-adj] noisy, annoying

## 32. な-Adjectives

- げんき - [na-adj] healthy, energetic
- しずか - [na-adj] quiet
- にぎやか - [na-adj] lively, bustling
- きれい - [na-adj] pretty, clean
- しんせつ - [na-adj] kind
- ひま - [na-adj] free time
- たいへん - [na-adj] tough, difficult
- だいじょうぶ - [na-adj] alright, OK
- べんり - [na-adj] convenient
- ふべん - [na-adj] inconvenient
- ゆうめい - [na-adj] famous
- じょうず - [na-adj] skilled
- へた - [na-adj] unskilled
- すき - [na-adj] liked
- きらい - [na-adj] disliked
- だいすき - [na-adj] love
- だいきらい - [na-adj] hate
- おなじ - [na-adj] same
- いろいろ - [na-adj] various
- りっぱ - [na-adj] splendid **[Ext]**
- かんたん - [na-adj] easy, simple
- けっこう - [na-adj] fine, sufficient
- たいせつ - [na-adj] important
- だいじ - [na-adj] important
- あんぜん - [na-adj] safe
- じょうぶ - [na-adj] sturdy
- いや - [na-adj] unpleasant, disagreeable

## 33. Adverbs

- とても - [adv.] very
- すごく - [adv.] very (casual)
- すこし - [adv.] a little
- ちょっと - [adv.] a little
- たくさん - [adv.] many, a lot
- おおぜい - [adv.] a lot of (people)
- だいたい - [adv.] generally, roughly
- ぜんぶ - [adv.] all
- みんな / みな - [n.] everyone
- もう - [adv.] already
- まだ - [adv.] still, not yet
- もうすこし - [adv.] a little more
- もっと - [adv.] more
- 一番 (いちばん) - [adv.] most, number one
- とくに - [adv.] especially
- ほんとうに - [adv.] truly, really
- ゆっくり - [adv.] slowly
- すぐ - [adv.] soon
- たぶん - [adv.] probably
- いっしょに - [adv.] together
- 一人で (ひとりで) - [adv.] alone
- じぶんで - [adv.] by oneself
- かならず - [adv.] surely, definitely
- きっと - [adv.] surely
- もちろん - [adv.] of course
- どうぞ - [exp.] please (offering)
- どうも - [exp.] thanks, indeed
- どうぞよろしく - [exp.] please treat me well
- どう - [adv.] how
- なぜ - [adv.] why
- どうして - [adv.] why
- まっすぐ - [adv.] straight ahead
- もういちど - [adv.] once more
- まず - [adv.] first of all
- では / じゃ - [exp.] well then
- もしもし - [exp.] hello (telephone)

## 34. Conjunctions

- そして - [conj.] and then
- それから - [conj.] and then, after that
- それで - [conj.] and so
- でも - [conj.] but, however
- しかし - [conj.] but, however
- けれど / けれども / けど - [conj.] but
- が - [conj.] but (clause-connector)
- から - [conj.] because, so
- だから - [conj.] therefore
- ですから - [conj.] therefore (polite)
- それに - [conj.] moreover
- じゃあ / では - [exp.] well then
- ところで - [conj.] by the way
- または - [conj.] or

## 35. Particles (functional vocabulary)

- は - [part.] topic marker
- が - [part.] subject marker
- を - [part.] object marker
- に - [part.] to, at, in (target / time)
- で - [part.] at, by, with (location of action / means)
- へ - [part.] to (direction)
- と - [part.] and, with
- か - [part.] question marker
- も - [part.] also
- や - [part.] and (non-exhaustive)
- の - [part.] of, possessive / nominalizer
- から - [part.] from, because
- まで - [part.] until
- ね - [part.] sentence-final (agreement)
- よ - [part.] sentence-final (assertion)
- だけ - [part.] only
- しか - [part.] only (with negative)
- ぐらい / くらい - [part.] about
- ごろ - [part.] around (time)
- ずつ - [part.] each
- など - [part.] etc.

## 36. Greetings and Set Phrases

- おはようございます - [exp.] good morning
- こんにちは - [exp.] hello / good afternoon
- こんばんは - [exp.] good evening
- おやすみなさい - [exp.] good night
- さようなら - [exp.] goodbye
- しつれいします - [exp.] excuse me / pardon me
- しつれいしました - [exp.] excuse me (past)
- ありがとう - [exp.] thanks
- ありがとうございます - [exp.] thank you
- どういたしまして - [exp.] you're welcome
- すみません - [exp.] excuse me / sorry
- ごめんなさい - [exp.] I'm sorry
- おねがいします - [exp.] please
- いただきます - [exp.] said before eating
- ごちそうさまでした - [exp.] said after eating **[Cul]**
- いってきます - [exp.] I'm off (and will return) **[Cul]**
- いってらっしゃい - [exp.] see you / take care **[Cul]**
- ただいま - [exp.] I'm home **[Cul]**
- おかえりなさい - [exp.] welcome back **[Cul]**
- はじめまして - [exp.] nice to meet you
- どうぞよろしく - [exp.] pleased to meet you
- おげんきですか - [exp.] how are you?
- おかげさまで - [exp.] thanks to you **[Cul]**
- いらっしゃいませ - [exp.] welcome (to a shop) **[Cul]**
- どうぞ - [exp.] please (offering)
- どうも - [exp.] thanks
- もしもし - [exp.] hello (phone)

## 37. Common Nouns - Miscellaneous

- もの - [n.] thing
- こと - [n.] thing (intangible)
- 名前 (なまえ) - [n.] name
- ことば - [n.] word
- 話 (はなし) - [n.] story, talk
- しごと - [n.] work, job
- やくそく - [n.] promise, appointment
- ようじ - [n.] errand
- もんだい - [n.] problem
- しゅみ - [n.] hobby
- りょこう - [n.] travel
- さんぽ - [n.] walk
- うんどう - [n.] exercise
- ゲーム - [n.] game
- スポーツ - [n.] sport
- しあい - [n.] match, game
- ニュース - [n.] news
- パーティー - [n.] party
- きって - [n.] stamp
- はがき - [n.] postcard
- てがみ - [n.] letter
- きっぷ - [n.] ticket
- おみやげ - [n.] souvenir (also in §22 - listed here for thematic completeness) **[Cul]**
- プレゼント - [n.] present, gift
- りゅうがく - [n.] study abroad **[Ext]**
- けっこん - [n.] marriage
- しゃしん - [n.] photograph
- りょかん - [n.] Japanese inn (also in §13) **[Cul]**
- かぜ - [n.] cold (illness)
- びょうき - [n.] illness
- くすり - [n.] medicine
- けが - [n.] injury
- おゆ - [n.] hot water
- おふろ - [n.] bath (also in §13)
- シャワー - [n.] shower
> **Legacy items note:** The items below tagged **[Cul]** (マッチ, フィルム, レコード, テープレコーダー, はいざら) are largely obsolete in modern Japan but appear in some older N5 study sources. Recognize them; do not prioritize.

- マッチ - [n.] match (lighting) **[Cul]**
- たばこ - [n.] cigarette
- はいざら - [n.] ashtray **[Cul]**
- スリッパ - [n.] slippers
- ティッシュ - [n.] tissue
- フィルム - [n.] film **[Cul]**
- レコード - [n.] record **[Cul]**
- テープ - [n.] tape (also in §26)
- よてい - [n.] plan, schedule
- じかんわり - [n.] timetable
- はこ - [n.] box
- 半分 (はんぶん) - [n.] half
- はたち - [n.] 20 years old (special reading)
- へん - [n.] area, vicinity
- ほか - [n.] other (place / thing / person)
- ほんとう - [n.] truth, reality
- なつやすみ - [n.] summer vacation
- やすみ - [n.] rest, holiday (noun form of やすむ)
- りょうり - [n.] cuisine, cooking
- ペット - [n.] pet
- カレンダー - [n.] calendar
- かてい - [n.] household, home life
- かびん - [n.] vase
- かた - [n.] way of doing (e.g., たべかた = how to eat)
- おくさん - [n.] wife (someone else's; polite)
- 先 (さき) - [n.] earlier, ahead, previous
- せびろ - [n.] business suit (older term, replaced by スーツ in modern usage) **[Ext]**
- 大きな (おおきな) - [n.] big (variant adjectival form of 大きい)
- たて - [n.] length, height
- ゆうべ - [n.] last night
- にっき - [n.] diary, journal
- さくぶん - [n.] composition, written essay
- じびき - [n.] dictionary (older term, alt for じしょ) **[Ext]**
- テープレコーダー - [n.] tape recorder **[Cul]**
- ストーブ - [n.] heater, stove **[Cul]**
- ページ - [n.] page
- クラス - [n.] class
- グラム - [n.] gram
- メートル - [n.] metre, meter
- キログラム - [n.] kilogram
- キロメートル - [n.] kilometre, kilometer

## 38. Sounds and Voice

- こえ - [n.] voice
- おと - [n.] sound
- うた - [n.] song

## 39. Function / Filler Expressions

- えーと - [exp.] um, let me see
- あの - [exp.] um (hesitation)
- そうですね - [exp.] let me think / that's right
- そうですか - [exp.] is that so?
- いいえ - [exp.] no
- はい - [exp.] yes
- ええ - [exp.] yes (casual)
- うん - [exp.] yeah (informal)
- ううん - [exp.] no (informal)
- やはり / やっぱり - [adv.] as expected
- さあ - [exp.] well... (filler / hesitation)
- いかが - [exp.] how (polite form of どう)
- それでは - [exp.] in that case, well then

## 40. Misc Useful Items

- もの - [n.] thing (physical) (also in §37)
- こと - [n.] thing (abstract) (also in §37)
- ばしょ - [n.] place
- ばあい - [n.] case, situation
- ほう - [n.] direction, side
- とき - [n.] time, occasion (also in §10)
- 番号 (ばんごう) - [n.] number (also in §24)
- じゅうしょ - [n.] address
- 名前 (なまえ) - [n.] name (also in §37)
- ねんれい - [n.] age
- しごと - [n.] job (also in §37)
- 学校 (がっこう) - [n.] school (also in §13)
- しゅみ - [n.] hobby (also in §37)
- しゅっしん - [n.] hometown / origin

---

## Notes on Coverage

- This list intentionally cross-lists some items (e.g., 名前, しごと, おみやげ) under multiple thematic sections. Each cross-listing is annotated; they are not accidental duplicates.
- Items tagged **[Ext]** or **[Cul]** are kept for completeness but should be deprioritized when planning a focused N5 study schedule. Strip the `[Ext]` and `[Cul]` lines for a tighter "exam-only" subset.
- Kanji rendering follows the rule stated above: only kanji from `kanji_n5.md` appear; everything else is in hiragana / katakana.


---

## N4 NEW VOCABULARY

631 entries from the alphabetical a-h sample, distributed across 18 thematic sections.

## 1. People and relationships

- 赤ちゃん (あかちゃん) - [n.] baby; infant [tier:core_n4] [examples:0]
- 赤ん坊 (あかんぼう) - [n.] baby; infant [tier:core_n4] [examples:0]
- アナウンサー (アナウンサー) - [n.] announcer [tier:core_n4] [examples:0]
- あんな (あんな) - [dem.] such [tier:core_n4] [examples:0]
- 僕 (ぼく) - [pron.] I (used by males) [tier:core_n4] [examples:0]
- 部長 (ぶちょう) - [n.] manager; head of section/department [tier:core_n4] [examples:0]
- ちゃん (ちゃん) - [n.] suffix for familiar female person [tier:core_n4] [examples:0]
- 男性 (だんせい) - [n.] man; male [tier:core_n4] [examples:0]
- 泥棒 (どろぼう) - [n.] thief [tier:core_n4] [examples:0]
- ご主人 (ごしゅじん) - [n.] your husband; her husband [tier:core_n4] [examples:0]
- 歯医者 (はいしゃ) - [n.] dentist [tier:core_n4] [examples:0]
- 色んな (いろんな) - [dem.] various [tier:core_n4] [examples:0]
- 女性 (じょせい) - [n.] woman; female [tier:core_n4] [examples:0]
- 課長 (かちょう) - [n.] section manager; section chief [tier:core_n4] [examples:0]
- 家内 (かない) - [n.] (my) wife; inside the home [tier:core_n4] [examples:0]
- 看護婦 (かんごふ) - [n.] female nurse [tier:core_n4] [examples:0]
- 彼女 (かのじょ) - [pron.] she; her [tier:core_n4] [examples:0]
- 彼 (かれ) - [pron.] he; him; his [tier:core_n4] [examples:0]
- 彼ら (かれら) - [pron.] they; them [tier:core_n4] [examples:0]
- 君 (きみ) - [pron.] You [tier:core_n4] [examples:0]
- 子 (こ) - [n.] child [tier:core_n4] [examples:0]
- 夫 (おっと) - [n.] husband [tier:core_n4] [examples:0]
- 親 (おや) - [n.] parents [tier:core_n4] [examples:0]
- 社長 (しゃちょう) - [n.] company president; manager [tier:core_n4] [examples:0]
- 祖母 (そぼ) - [n.] grandmother [tier:core_n4] [examples:0]
- 祖父 (そふ) - [n.] grandfather [tier:core_n4] [examples:0]
- そんな (そんな) - [dem.] that sort of [tier:core_n4] [examples:0]
- 妻 (つま) - [n.] (humble) wife [tier:core_n4] [examples:0]

## 2. Home and daily life

- 美術館 (びじゅつかん) - [n.] art gallery; art museum [tier:core_n4] [examples:0]
- ビル (ビル) - [n.] building [tier:core_n4] [examples:0]
- 道具 (どうぐ) - [n.] tool [tier:core_n4] [examples:0]
- 布団 (ふとん) - [n.] Japanese bedding, futon [tier:core_n4] [examples:0]
- ガソリン (ガソリン) - [n.] gasoline; petrol [tier:core_n4] [examples:0]
- 下宿 (げしゅく) - [n.] lodging [tier:core_n4] [examples:0]
- ごみ (ごみ) - [n.] rubbish [tier:core_n4] [examples:0]
- 二階建て (にかいだて) - [n.] two-storied building [tier:core_n4] [examples:0]
- 旅館 (りょかん) - [n.] traditional inn; Japanese-style lodging [tier:core_n4] [examples:0]

## 3. School and study

- 文学 (ぶんがく) - [n.] literature [tier:core_n4] [examples:0]
- 文化 (ぶんか) - [n.] culture [tier:core_n4] [examples:0]
- 文法 (ぶんぽう) - [n.] grammar [tier:core_n4] [examples:0]
- 地理 (ちり) - [n.] geography [tier:core_n4] [examples:0]
- 中学校 (ちゅうがっこう) - [n.] junior high school; middle school [tier:core_n4] [examples:0]
- 大学生 (だいがくせい) - [n.] university student; college student [tier:core_n4] [examples:0]
- 復習 (ふくしゅう) - [n.] review of learned material; revision [tier:core_n4] [examples:0]
- 高校 (こうこう) - [n.] senior high school; high school [tier:core_n4] [examples:0]
- 高校生 (こうこうせい) - [n.] high school student [tier:core_n4] [examples:0]
- 高等学校 (こうとうがっこう) - [n.] high school [tier:core_n4] [examples:0]
- 入学 (にゅうがく) - [n.] entry to school or university; enrollment [tier:core_n4] [examples:0]
- 小学校 (しょうがっこう) - [n.] elementary school [tier:core_n4] [examples:0]

## 4. Work and society

- 挨拶 (あいさつ) - [n.] to greet [tier:core_n4] [examples:0]
- 案内 (あんない) - [n.] to guide [tier:core_n4] [examples:0]
- 遊び (あそび) - [n.] playing [tier:core_n4] [examples:0]
- 倍 (ばい) - [n.] double [tier:core_n4] [examples:0]
- 番組 (ばんぐみ) - [n.] program (e.g. TV) [tier:core_n4] [examples:0]
- 場所 (ばしょ) - [n.] place [tier:core_n4] [examples:0]
- ベル (ベル) - [n.] bell [tier:core_n4] [examples:0]
- 貿易 (ぼうえき) - [n.] trade [tier:core_n4] [examples:0]
- チェック (チェック) - [n.] to check [tier:core_n4] [examples:0]
- 力 (ちから) - [n.] energy; force; strength; might; power [tier:core_n4] [examples:0]
- 大体 (だいたい) - [n.] roughly [tier:core_n4] [examples:0]
- 暖房 (だんぼう) - [n.] heating [tier:core_n4] [examples:0]
- 電報 (でんぽう) - [n.] telegram [tier:core_n4] [examples:0]
- 電灯 (でんとう) - [n.] electric light [tier:core_n4] [examples:0]
- 動物園 (どうぶつえん) - [n.] zoo; zoological gardens [tier:core_n4] [examples:0]
- 枝 (えだ) - [n.] branch [tier:core_n4] [examples:0]
- ファックス (ファックス) - [n.] fax [tier:core_n4] [examples:0]
- 船 (ふね) - [n.] ship [tier:core_n4] [examples:0]
- 普通 (ふつう) - [n.] usually [tier:core_n4] [examples:0]
- ガラス (ガラス) - [n.] a glass [tier:core_n4] [examples:0]
- ガス (ガス) - [n.] petrol [tier:core_n4] [examples:0]
- 原因 (げんいん) - [n.] cause [tier:core_n4] [examples:0]
- 技術 (ぎじゅつ) - [n.] art, technology, skill [tier:core_n4] [examples:0]
- ご存じ (ごぞんじ) - [n.] knowing [tier:core_n4] [examples:0]
- 拝見 (はいけん) - [n.] seeing; looking at [tier:core_n4] [examples:0]
- 発音 (はつおん) - [n.] pronunciation [tier:core_n4] [examples:0]
- 返事 (へんじ) - [n.] reply; answer; response [tier:core_n4] [examples:0]
- 火 (ひ) - [n.] fire [tier:core_n4] [examples:0]
- 髭 (ひげ) - [n.] beard [tier:core_n4] [examples:0]
- 光 (ひかり) - [n.] light [tier:core_n4] [examples:0]
- 引き出し (ひきだし) - [n.] drawer [tier:core_n4] [examples:0]
- 昼休み (ひるやすみ) - [n.] lunch break; noon recess [tier:core_n4] [examples:0]
- 翻訳 (ほんやく) - [n.] translation [tier:core_n4] [examples:0]
- 星 (ほし) - [n.] star [tier:core_n4] [examples:0]
- 法律 (ほうりつ) - [n.] law [tier:core_n4] [examples:0]
- 放送 (ほうそう) - [n.] to broadcast [tier:core_n4] [examples:0]
- 以外 (いがい) - [n.] with the exception of; excepting [tier:core_n4] [examples:0]
- 以上 (いじょう) - [n.] ... and more; ... and upwards [tier:core_n4] [examples:0]
- 以下 (いか) - [n.] not exceeding [tier:core_n4] [examples:0]
- 生き物 (いきもの) - [n.] living thing [tier:core_n4] [examples:0]
- 以内 (いない) - [n.] within [tier:core_n4] [examples:0]
- 田舎 (いなか) - [n.] countryside [tier:core_n4] [examples:0]
- 石 (いし) - [n.] stone [tier:core_n4] [examples:0]
- 糸 (いと) - [n.] thread [tier:core_n4] [examples:0]
- ジャム (ジャム) - [n.] jam [tier:core_n4] [examples:0]
- 字 (じ) - [n.] character [tier:core_n4] [examples:0]
- 時代 (じだい) - [n.] period [tier:core_n4] [examples:0]
- 事故 (じこ) - [n.] accident [tier:core_n4] [examples:0]
- 事務所 (じむしょ) - [n.] office [tier:core_n4] [examples:0]
- 神社 (じんじゃ) - [n.] Shinto shrine [tier:core_n4] [examples:0]
- 人口 (じんこう) - [n.] population [tier:core_n4] [examples:0]
- 人生 (じんせい) - [n.] human life [tier:core_n4] [examples:0]
- 地震 (じしん) - [n.] earthquake [tier:core_n4] [examples:0]
- 辞典 (じてん) - [n.] dictionary [tier:core_n4] [examples:0]
- 準備 (じゅんび) - [n.] to prepare [tier:core_n4] [examples:0]
- 柔道 (じゅうどう) - [n.] judo [tier:core_n4] [examples:0]
- 住所 (じゅうしょ) - [n.] address [tier:core_n4] [examples:0]
- カーテン (カーテン) - [n.] curtain [tier:core_n4] [examples:0]
- 壁 (かべ) - [n.] wall [tier:core_n4] [examples:0]
- 帰り (かえり) - [n.] return; coming back [tier:core_n4] [examples:0]
- 科学 (かがく) - [n.] science [tier:core_n4] [examples:0]
- 鏡 (かがみ) - [n.] mirror [tier:core_n4] [examples:0]
- 海岸 (かいがん) - [n.] coast [tier:core_n4] [examples:0]
- 会議 (かいぎ) - [n.] meeting; conference; session [tier:core_n4] [examples:0]
- 会議室 (かいぎしつ) - [n.] conference room; conference hall [tier:core_n4] [examples:0]
- 会場 (かいじょう) - [n.] assembly hall; meeting place; venue [tier:core_n4] [examples:0]
- 会話 (かいわ) - [n.] conversation [tier:core_n4] [examples:0]
- 火事 (かじ) - [n.] fire [tier:core_n4] [examples:0]
- 格好 (かっこう) - [n.] appearance [tier:core_n4] [examples:0]
- 髪 (かみ) - [n.] hair [tier:core_n4] [examples:0]
- 関係 (かんけい) - [n.] relationship [tier:core_n4] [examples:0]
- 形 (かたち) - [n.] shape [tier:core_n4] [examples:0]
- 毛 (け) - [n.] hair or fur [tier:core_n4] [examples:0]
- ケーキ (ケーキ) - [n.] cake [tier:core_n4] [examples:0]
- 怪我 (けが) - [n.] to injure [tier:core_n4] [examples:0]
- 計画 (けいかく) - [n.] to plan [tier:core_n4] [examples:0]
- 経験 (けいけん) - [n.] to experience [tier:core_n4] [examples:0]
- 警察 (けいさつ) - [n.] police [tier:core_n4] [examples:0]
- 経済 (けいざい) - [n.] finance, economy [tier:core_n4] [examples:0]
- 見物 (けんぶつ) - [n.] sightseeing; visit [tier:core_n4] [examples:0]
- 喧嘩 (けんか) - [n.] to quarrel [tier:core_n4] [examples:0]
- 研究 (けんきゅう) - [n.] research [tier:core_n4] [examples:0]
- 研究室 (けんきゅうしつ) - [n.] laboratory [tier:core_n4] [examples:0]
- 消しゴム (けしごむ) - [n.] eraser [tier:core_n4] [examples:0]
- 景色 (けしき) - [n.] scenery [tier:core_n4] [examples:0]
- 気 (き) - [n.] spirit [tier:core_n4] [examples:0]
- 機会 (きかい) - [n.] chance; opportunity [tier:core_n4] [examples:0]
- 着物 (きもの) - [n.] kimono; Japanese traditional clothing [tier:core_n4] [examples:0]
- 近所 (きんじょ) - [n.] neighbourhood [tier:core_n4] [examples:0]
- 絹 (きぬ) - [n.] silk [tier:core_n4] [examples:0]
- 季節 (きせつ) - [n.] season [tier:core_n4] [examples:0]
- 規則 (きそく) - [n.] rule [tier:core_n4] [examples:0]
- 心 (こころ) - [n.] heart [tier:core_n4] [examples:0]
- 国際 (こくさい) - [n.] international [tier:core_n4] [examples:0]
- コンピュータ (コンピュータ) - [n.] computer [tier:core_n4] [examples:0]
- コンサート (コンサート) - [n.] concert [tier:core_n4] [examples:0]
- 故障 (こしょう) - [n.] to break-down [tier:core_n4] [examples:0]
- 答え (こたえ) - [n.] response [tier:core_n4] [examples:0]
- 小鳥 (ことり) - [n.] small bird [tier:core_n4] [examples:0]
- 校長 (こうちょう) - [n.] principal; headmaster [tier:core_n4] [examples:0]
- 講堂 (こうどう) - [n.] auditorium [tier:core_n4] [examples:0]
- 郊外 (こうがい) - [n.] suburb; residential area [tier:core_n4] [examples:0]
- 講義 (こうぎ) - [n.] lecture [tier:core_n4] [examples:0]
- 工業 (こうぎょう) - [n.] industry [tier:core_n4] [examples:0]
- 工場 (こうじょう) - [n.] factory [tier:core_n4] [examples:0]
- 公務員 (こうむいん) - [n.] government worker [tier:core_n4] [examples:0]
- 交通 (こうつう) - [n.] traffic [tier:core_n4] [examples:0]
- 首 (くび) - [n.] neck [tier:core_n4] [examples:0]
- 草 (くさ) - [n.] grass [tier:core_n4] [examples:0]
- 空気 (くうき) - [n.] air [tier:core_n4] [examples:0]
- 客 (きゃく) - [n.] guest; customer [tier:core_n4] [examples:0]
- 教育 (きょういく) - [n.] education [tier:core_n4] [examples:0]
- 教会 (きょうかい) - [n.] church; congregation [tier:core_n4] [examples:0]
- 興味 (きょうみ) - [n.] interest (in something) [tier:core_n4] [examples:0]
- 競争 (きょうそう) - [n.] competition [tier:core_n4] [examples:0]
- 急行 (きゅうこう) - [n.] hurrying; rushing; hastening [tier:core_n4] [examples:0]
- 漫画 (まんが) - [n.] comic [tier:core_n4] [examples:0]
- 真ん中 (まんなか) - [n.] middle; centre; center [tier:core_n4] [examples:0]
- 周り (まわり) - [n.] around [tier:core_n4] [examples:0]
- 港 (みなと) - [n.] harbour [tier:core_n4] [examples:0]
- 味噌 (みそ) - [n.] fermented condiment made from soybeans [tier:core_n4] [examples:0]
- 都 (みやこ) - [n.] capital [tier:core_n4] [examples:0]
- 湖 (みずうみ) - [n.] lake [tier:core_n4] [examples:0]
- 木綿 (もめん) - [n.] cotton (material) [tier:core_n4] [examples:0]
- 虫 (むし) - [n.] insect [tier:core_n4] [examples:0]
- 息子 (むすこ) - [n.] son [tier:core_n4] [examples:0]
- 娘 (むすめ) - [n.] daughter [tier:core_n4] [examples:0]
- 生 (なま) - [n.] raw [tier:core_n4] [examples:0]
- 寝坊 (ねぼう) - [n.] sleeping in late; oversleeping [tier:core_n4] [examples:0]
- 熱 (ねつ) - [n.] fever [tier:core_n4] [examples:0]
- 人形 (にんぎょう) - [n.] doll [tier:core_n4] [examples:0]
- 匂い (におい) - [n.] a smell [tier:core_n4] [examples:0]
- 喉 (のど) - [n.] throat [tier:core_n4] [examples:0]
- 乗り物 (のりもの) - [n.] vehicle [tier:core_n4] [examples:0]
- 入院 (にゅういん) - [n.] hospitalization [tier:core_n4] [examples:0]
- 踊り (おどり) - [n.] a dance [tier:core_n4] [examples:0]
- お祝い (おいわい) - [n.] congratulation [tier:core_n4] [examples:0]
- お嬢さん (おじょうさん) - [n.] (another's) daughter [tier:core_n4] [examples:0]
- 億 (おく) - [n.] one hundred million [tier:core_n4] [examples:0]
- 屋上 (おくじょう) - [n.] rooftop [tier:core_n4] [examples:0]
- 贈り物 (おくりもの) - [n.] present; gift [tier:core_n4] [examples:0]
- お祭り (おまつり) - [n.] festival [tier:core_n4] [examples:0]
- お見舞い (おみまい) - [n.] visiting ill or distressed people [tier:core_n4] [examples:0]
- お土産 (おみやげ) - [n.] souvenir [tier:core_n4] [examples:0]
- おもちゃ (おもちゃ) - [n.] toy [tier:core_n4] [examples:0]
- 表 (おもて) - [n.] the front [tier:core_n4] [examples:0]
- オートバイ (オートバイ) - [n.] motorcycle [tier:core_n4] [examples:0]
- お礼 (おれい) - [n.] thanks [tier:core_n4] [examples:0]
- 押し入れ (おしいれ) - [n.] closet [tier:core_n4] [examples:0]
- お宅 (おたく) - [n.] your home [tier:core_n4] [examples:0]
- 音 (おと) - [n.] sound; note [tier:core_n4] [examples:0]
- お釣り (おつり) - [n.] change (for a purchase) [tier:core_n4] [examples:0]
- 終わり (おわり) - [n.] the end [tier:core_n4] [examples:0]
- 泳ぎ方 (およぎかた) - [n.] way of swimming [tier:core_n4] [examples:0]
- パソコン (パソコン) - [n.] personal computer [tier:core_n4] [examples:0]
- ピアノ (ピアノ) - [n.] piano [tier:core_n4] [examples:0]
- プレゼント (プレゼント) - [n.] present; gift [tier:core_n4] [examples:0]
- レジ (レジ) - [n.] cashier [tier:core_n4] [examples:0]
- 歴史 (れきし) - [n.] history [tier:core_n4] [examples:0]
- 連絡 (れんらく) - [n.] to contact; to get in touch [tier:core_n4] [examples:0]
- レポート (レポート) - [n.] report [tier:core_n4] [examples:0]
- 利用 (りよう) - [n.] use; utilization; application [tier:core_n4] [examples:0]
- 理由 (りゆう) - [n.] reason [tier:core_n4] [examples:0]
- 留守 (るす) - [n.] absence [tier:core_n4] [examples:0]
- 両方 (りょうほう) - [n.] both sides [tier:core_n4] [examples:0]
- 最後 (さいご) - [n.] end; last [tier:core_n4] [examples:0]
- 坂 (さか) - [n.] slope; hill [tier:core_n4] [examples:0]
- サンダル (サンダル) - [n.] sandal [tier:core_n4] [examples:0]
- サンドイッチ (サンドイッチ) - [n.] sandwich [tier:core_n4] [examples:0]
- 産業 (さんぎょう) - [n.] industry [tier:core_n4] [examples:0]
- サラダ (サラダ) - [n.] salad [tier:core_n4] [examples:0]
- 生物 (せいぶつ) - [n.] living thing [tier:core_n4] [examples:0]
- 政治 (せいじ) - [n.] politics [tier:core_n4] [examples:0]
- 生活 (せいかつ) - [n.] to live [tier:core_n4] [examples:0]
- 生命 (せいめい) - [n.] life [tier:core_n4] [examples:0]
- 生産 (せいさん) - [n.] production [tier:core_n4] [examples:0]
- 西洋 (せいよう) - [n.] the west; Western countries [tier:core_n4] [examples:0]
- 世界 (せかい) - [n.] the world [tier:core_n4] [examples:0]
- 席 (せき) - [n.] seat [tier:core_n4] [examples:0]
- 線 (せん) - [n.] line [tier:core_n4] [examples:0]
- 先輩 (せんぱい) - [n.] senior [tier:core_n4] [examples:0]
- 戦争 (せんそう) - [n.] war [tier:core_n4] [examples:0]
- 説明 (せつめい) - [n.] explanation [tier:core_n4] [examples:0]
- 社会 (しゃかい) - [n.] society; public; community [tier:core_n4] [examples:0]
- 市 (し) - [n.] city [tier:core_n4] [examples:0]
- 試合 (しあい) - [n.] match, game [tier:core_n4] [examples:0]
- 仕方 (しかた) - [n.] way; method [tier:core_n4] [examples:0]
- 試験 (しけん) - [n.] examination [tier:core_n4] [examples:0]
- 島 (しま) - [n.] island [tier:core_n4] [examples:0]
- 市民 (しみん) - [n.] citizen [tier:core_n4] [examples:0]
- 品物 (しなもの) - [n.] goods; article; thing [tier:core_n4] [examples:0]
- 新聞社 (しんぶんしゃ) - [n.] newspaper company [tier:core_n4] [examples:0]
- 失敗 (しっぱい) - [n.] failure [tier:core_n4] [examples:0]
- 下着 (したぎ) - [n.] underwear [tier:core_n4] [examples:0]
- 紹介 (しょうかい) - [n.] introduction [tier:core_n4] [examples:0]
- 小説 (しょうせつ) - [n.] novel [tier:core_n4] [examples:0]
- 習慣 (しゅうかん) - [n.] habit; custom [tier:core_n4] [examples:0]
- ソフト (ソフト) - [n.] soft [tier:core_n4] [examples:0]
- 卒業 (そつぎょう) - [n.] graduation [tier:core_n4] [examples:0]
- 相談 (そうだん) - [n.] to discuss [tier:core_n4] [examples:0]
- 水道 (すいどう) - [n.] water supply [tier:core_n4] [examples:0]
- 水泳 (すいえい) - [n.] swimming [tier:core_n4] [examples:0]
- スクリーン (スクリーン) - [n.] screen [tier:core_n4] [examples:0]
- 隅 (すみ) - [n.] corner; nook [tier:core_n4] [examples:0]
- 砂 (すな) - [n.] sand [tier:core_n4] [examples:0]
- すり (すり) - [n.] pickpocket [tier:core_n4] [examples:0]
- スーツケース (スーツケース) - [n.] suitcase [tier:core_n4] [examples:0]
- ステレオ (ステレオ) - [n.] stereo [tier:core_n4] [examples:0]
- 数学 (すうがく) - [n.] mathematics; arithmetic [tier:core_n4] [examples:0]
- スーツ (スーツ) - [n.] suit [tier:core_n4] [examples:0]
- 退院 (たいいん) - [n.] leaving hospital; discharge [tier:core_n4] [examples:0]
- 台風 (たいふう) - [n.] typhoon [tier:core_n4] [examples:0]
- タイプ (タイプ) - [n.] type, style [tier:core_n4] [examples:0]
- 棚 (たな) - [n.] shelves [tier:core_n4] [examples:0]
- 誕生 (たんじょう) - [n.] birth [tier:core_n4] [examples:0]
- 畳 (たたみ) - [n.] Japanese straw mat [tier:core_n4] [examples:0]
- 手袋 (てぶくろ) - [n.] glove [tier:core_n4] [examples:0]
- テキスト (テキスト) - [n.] text; textbook [tier:core_n4] [examples:0]
- 点 (てん) - [n.] point; dot [tier:core_n4] [examples:0]
- テニス (テニス) - [n.] tennis [tier:core_n4] [examples:0]
- 展覧会 (てんらんかい) - [n.] exhibition [tier:core_n4] [examples:0]
- 寺 (てら) - [n.] temple [tier:core_n4] [examples:0]
- 床屋 (とこや) - [n.] barber [tier:core_n4] [examples:0]
- 遠く (とおく) - [n.] distant [tier:core_n4] [examples:0]
- 都合 (つごう) - [n.] convenience [tier:core_n4] [examples:0]
- 月 (つき) - [n.] moon [tier:core_n4] [examples:0]
- 腕 (うで) - [n.] arm [tier:core_n4] [examples:0]
- 受付 (うけつけ) - [n.] reception (desk) [tier:core_n4] [examples:0]
- 生まれ (うまれ) - [n.] birth [tier:core_n4] [examples:0]
- 運転手 (うんてんしゅ) - [n.] driver; chauffeur [tier:core_n4] [examples:0]
- 裏 (うら) - [n.] reverse side [tier:core_n4] [examples:0]
- 売り場 (うりば) - [n.] selling area [tier:core_n4] [examples:0]
- 嘘 (うそ) - [n.] a lie [tier:core_n4] [examples:0]
- ワープロ (ワープロ) - [n.] word processor [tier:core_n4] [examples:0]
- 割合 (わりあい) - [n.] rate; ratio [tier:core_n4] [examples:0]
- 忘れ物 (わすれもの) - [n.] lost article [tier:core_n4] [examples:0]
- 約束 (やくそく) - [n.] promise [tier:core_n4] [examples:0]
- 予習 (よしゅう) - [n.] preparation for a lesson [tier:core_n4] [examples:0]
- 予定 (よてい) - [n.] plan [tier:core_n4] [examples:0]
- 用 (よう) - [n.] business; task; errand [tier:core_n4] [examples:0]
- 用意 (ようい) - [n.] preparation; arrangements [tier:core_n4] [examples:0]
- 用事 (ようじ) - [n.] tasks; things to do [tier:core_n4] [examples:0]
- 予約 (よやく) - [n.] reservation [tier:core_n4] [examples:0]
- 湯 (ゆ) - [n.] hot water [tier:core_n4] [examples:0]
- 指 (ゆび) - [n.] finger [tier:core_n4] [examples:0]
- 指輪 (ゆびわ) - [n.] finger ring [tier:core_n4] [examples:0]
- 夢 (ゆめ) - [n.] dream [tier:core_n4] [examples:0]

## 5. Travel and transportation

- アフリカ (アフリカ) - [n.] Africa [tier:core_n4] [examples:0]
- アジア (アジア) - [n.] Asia [tier:core_n4] [examples:0]
- アメリカ (アメリカ) - [n.] America [tier:core_n4] [examples:0]
- 駐車場 (ちゅうしゃじょう) - [n.] parking lot [tier:core_n4] [examples:0]
- エスカレーター (エスカレーター) - [n.] escalator [tier:core_n4] [examples:0]
- ガソリンスタンド (ガソリンスタンド) - [n.] petrol station [tier:core_n4] [examples:0]
- 飛行場 (ひこうじょう) - [n.] airfield; airport [tier:core_n4] [examples:0]
- 空港 (くうこう) - [n.] airport [tier:core_n4] [examples:0]

## 6. Shopping and money

- アクセサリー (アクセサリー) - [n.] accessory [tier:core_n4] [examples:0]
- アルバイト (アルバイト) - [n.] part-time job [tier:core_n4] [examples:0]
- ハンドバッグ (ハンドバッグ) - [n.] handbag [tier:core_n4] [examples:0]
- 値段 (ねだん) - [n.] price; cost [tier:core_n4] [examples:0]
- 店員 (てにん) - [n.] employee; shop assistant; clerk [tier:core_n4] [examples:0]

## 7. Food and restaurants

- 味 (あじ) - [n.] flavor; taste; uniqueness; attractiveness; experience [tier:core_n4] [examples:0]
- アルコール (アルコール) - [n.] alcohol [tier:core_n4] [examples:0]
- ぶどう (ぶどう) - [n.] grapes [tier:core_n4] [examples:0]
- ごちそう (ごちそう) - [n.] a feast [tier:core_n4] [examples:0]
- 葉 (は) - [n.] leaves; leaf [tier:core_n4] [examples:0]
- 代わり (かわり) - [n.] instead; in place [tier:core_n4] [examples:0]
- 米 (こめ) - [n.] (husked grains of) rice [tier:core_n4] [examples:0]
- 食料品 (しょくりょうひん) - [n.] food; groceries [tier:core_n4] [examples:0]
- ステーキ (ステーキ) - [n.] steak [tier:core_n4] [examples:0]

## 8. Health and body

- 血 (ち) - [n.] blood [tier:core_n4] [examples:0]
- 注意 (ちゅうい) - [n.] caution [tier:core_n4] [examples:0]
- 注射 (ちゅうしゃ) - [n.] injection [tier:core_n4] [examples:0]
- 具合 (ぐあい) - [n.] condition; health [tier:core_n4] [examples:0]
- 医学 (いがく) - [n.] medical science; medicine [tier:core_n4] [examples:0]
- 冷房 (れいぼう) - [n.] air conditioning [tier:core_n4] [examples:0]
- 背中 (せなか) - [n.] back (of body) [tier:core_n4] [examples:0]

## 9. Weather and nature

- 遠慮 (えんりょ) - [n.] reserve; refraining [tier:core_n4] [examples:0]
- 花見 (はなみ) - [n.] cherry blossom viewing; flower viewing [tier:core_n4] [examples:0]
- 林 (はやし) - [n.] woods; forest [tier:core_n4] [examples:0]
- 汽車 (きしゃ) - [n.] train [tier:core_n4] [examples:0]
- 雲 (くも) - [n.] cloud [tier:core_n4] [examples:0]
- 森 (もり) - [n.] forest [tier:core_n4] [examples:0]
- 天気予報 (てんきよほう) - [n.] weather forecast [tier:core_n4] [examples:0]
- 特急 (とっきゅう) - [n.] limited express (train) [tier:core_n4] [examples:0]

## 10. Time and frequency

- 昼間 (ひるま) - [n.] daytime; during the day [tier:core_n4] [examples:0]
- 一度 (いちど) - [n.] once; one time [tier:core_n4] [examples:0]
- 今度 (こんど) - [n.] this time; next time [tier:core_n4] [examples:0]
- 今夜 (こにゃ) - [n.] this evening; tonight [tier:core_n4] [examples:0]
- 昔 (むかし) - [n.] olden days, former [tier:core_n4] [examples:0]
- パート (パート) - [n.] part; part time [tier:core_n4] [examples:0]
- 趣味 (しゅみ) - [n.] hobby; pastime; preference [tier:core_n4] [examples:0]

## 11. Feelings and opinions

- 意見 (いけん) - [n.] opinion; view; comment [tier:core_n4] [examples:0]
- 気分 (きぶん) - [n.] feeling; mood [tier:core_n4] [examples:0]
- 気持ち (きもち) - [n.] feeling [tier:core_n4] [examples:0]

## 12. Verbs (general)

- 上がる (あがる) - [v1] to rise [tier:core_n4] [examples:0]
- 挨拶する (あいさつする) - [v3] to greet [tier:core_n4] [examples:0]
- 案内する (あんないする) - [v3] to guide [tier:core_n4] [examples:0]
- アルバイトする (アルバイトする) - [v3] to part-time job [tier:core_n4] [examples:0]
- 集まる (あつまる) - [v1] to gather; to collect; to assemble [tier:core_n4] [examples:0]
- 集める (あつめる) - [v2] to collect; to assemble; to gather [tier:core_n4] [examples:0]
- 謝る (あやまる) - [v1] to apologize [tier:core_n4] [examples:0]
- 貿易する (ぼうえきする) - [v3] to trade [tier:core_n4] [examples:0]
- チェックする (チェックする) - [v3] to check [tier:core_n4] [examples:0]
- 注意する (ちゅういする) - [v3] to caution [tier:core_n4] [examples:0]
- 注射する (ちゅうしゃする) - [v3] to injection [tier:core_n4] [examples:0]
- 暖房する (だんぼうする) - [v3] to heating [tier:core_n4] [examples:0]
- 遠慮する (えんりょする) - [v3] to reserve [tier:core_n4] [examples:0]
- 選ぶ (えらぶ) - [v1] to choose [tier:core_n4] [examples:0]
- ファックスする (ファックスする) - [v3] to fax [tier:core_n4] [examples:0]
- 増える (ふえる) - [v2] to increase [tier:core_n4] [examples:0]
- 復習する (ふくしゅうする) - [v3] to review of learned material [tier:core_n4] [examples:0]
- 踏む (ふむ) - [v1] to step on [tier:core_n4] [examples:0]
- 降り出す (ふりだす) - [v1] to start to rain [tier:core_n4] [examples:0]
- 太る (ふとる) - [v1] to become fat [tier:core_n4] [examples:0]
- 原因する (げんいんする) - [v3] to cause [tier:core_n4] [examples:0]
- 下宿する (げしゅくする) - [v3] to lodging [tier:core_n4] [examples:0]
- ごちそうする (ごちそうする) - [v3] to a feast [tier:core_n4] [examples:0]
- ご覧になる (ごらんになる) - [v1] (respectful) to see [tier:core_n4] [examples:0]
- 拝見する (はいけんする) - [v3] to seeing [tier:core_n4] [examples:0]
- 運ぶ (はこぶ) - [v1] to carry [tier:core_n4] [examples:0]
- 花見する (はなみする) - [v3] to cherry blossom viewing [tier:core_n4] [examples:0]
- 払う (はらう) - [v1] to pay [tier:core_n4] [examples:0]
- 発音する (はつおんする) - [v3] to pronunciation [tier:core_n4] [examples:0]
- 返事する (へんじする) - [v3] to reply [tier:core_n4] [examples:0]
- 冷える (ひえる) - [v2] to grow cold [tier:core_n4] [examples:0]
- 光る (ひかる) - [v1] to shine [tier:core_n4] [examples:0]
- 引き出す (ひきだす) - [v1] to withdraw [tier:core_n4] [examples:0]
- 引っ越す (ひっこす) - [v1] to move house [tier:core_n4] [examples:0]
- 開く (ひらく) - [v1] to open; to undo; to unseal; to unpack [tier:core_n4] [examples:0]
- 拾う (ひろう) - [v1] to pick up [tier:core_n4] [examples:0]
- 褒める (ほめる) - [v2] to praise [tier:core_n4] [examples:0]
- 翻訳する (ほんやくする) - [v3] to translation [tier:core_n4] [examples:0]
- 放送する (ほうそうする) - [v3] to broadcast [tier:core_n4] [examples:0]
- いじめる (いじめる) - [v2] to tease [tier:core_n4] [examples:0]
- 意見する (いけんする) - [v3] to opinion [tier:core_n4] [examples:0]
- 生きる (いきる) - [v2] to live [tier:core_n4] [examples:0]
- 祈る (いのる) - [v1] to pray [tier:core_n4] [examples:0]
- 急ぐ (いそぐ) - [v1] to hurry; to rush; to hasten [tier:core_n4] [examples:0]
- 頂く (いただく) - [v1] (humble) to receive [tier:core_n4] [examples:0]
- 致す (いたす) - [v1] (humble) to do [tier:core_n4] [examples:0]
- 準備する (じゅんびする) - [v3] to prepare [tier:core_n4] [examples:0]
- 変える (かえる) - [v2] to change; to transform [tier:core_n4] [examples:0]
- 会議する (かいぎする) - [v3] to meeting [tier:core_n4] [examples:0]
- 会話する (かいわする) - [v3] to conversation [tier:core_n4] [examples:0]
- 構う (かまう) - [v1] to mind [tier:core_n4] [examples:0]
- 噛む (かむ) - [v1] to bite; to chew [tier:core_n4] [examples:0]
- 考える (かんがえる) - [v2] to think [tier:core_n4] [examples:0]
- 関係する (かんけいする) - [v3] to relationship [tier:core_n4] [examples:0]
- 片付ける (かたづける) - [v2] to tidy up [tier:core_n4] [examples:0]
- 勝つ (かつ) - [v1] to win [tier:core_n4] [examples:0]
- 乾く (かわく) - [v1] to get dry [tier:core_n4] [examples:0]
- 変わる (かわる) - [v1] to change [tier:core_n4] [examples:0]
- 通う (かよう) - [v1] to commute [tier:core_n4] [examples:0]
- 飾る (かざる) - [v1] to decorate [tier:core_n4] [examples:0]
- 怪我する (けがする) - [v3] to injure [tier:core_n4] [examples:0]
- 計画する (けいかくする) - [v3] to plan [tier:core_n4] [examples:0]
- 経験する (けいけんする) - [v3] to experience [tier:core_n4] [examples:0]
- 見物する (けんぶつする) - [v3] to sightseeing [tier:core_n4] [examples:0]
- 喧嘩する (けんかする) - [v3] to quarrel [tier:core_n4] [examples:0]
- 研究する (けんきゅうする) - [v3] to research [tier:core_n4] [examples:0]
- 聞こえる (きこえる) - [v2] to be heard; to be audible [tier:core_n4] [examples:0]
- 決まる (きまる) - [v1] to be decided [tier:core_n4] [examples:0]
- 決める (きめる) - [v2] to decide [tier:core_n4] [examples:0]
- 込む (こむ) - [v1] to be crowded [tier:core_n4] [examples:0]
- 故障する (こしょうする) - [v3] to break-down [tier:core_n4] [examples:0]
- 講義する (こうぎする) - [v3] to lecture [tier:core_n4] [examples:0]
- 壊れる (こわれる) - [v2] to be broken [tier:core_n4] [examples:0]
- 壊す (こわす) - [v1] to break [tier:core_n4] [examples:0]
- 下さる (くださる) - [v1] (respectful) to give [tier:core_n4] [examples:0]
- 比べる (くらべる) - [v2] to compare [tier:core_n4] [examples:0]
- 暮れる (くれる) - [v2] to get dark [tier:core_n4] [examples:0]
- 教育する (きょういくする) - [v3] to education [tier:core_n4] [examples:0]
- 競争する (きょうそうする) - [v3] to competition [tier:core_n4] [examples:0]
- 急行する (きゅうこうする) - [v3] to hurrying [tier:core_n4] [examples:0]
- 間違える (まちがえる) - [v2] to make a mistake (in) [tier:core_n4] [examples:0]
- 参る (まいる) - [v1] (humble) to go; to come [tier:core_n4] [examples:0]
- 負ける (まける) - [v2] to lose [tier:core_n4] [examples:0]
- 間に合う (まにあう) - [v1] to be in time (for) [tier:core_n4] [examples:0]
- 回る (まわる) - [v1] to go around [tier:core_n4] [examples:0]
- 召し上がる (めしあがる) - [v1] to eat; to drink [tier:core_n4] [examples:0]
- 見える (みえる) - [v2] to be seen; to look; to seem [tier:core_n4] [examples:0]
- 見つかる (みつかる) - [v1] to be found; to be discovered [tier:core_n4] [examples:0]
- 見つける (みつける) - [v2] to discover; to find; to spot [tier:core_n4] [examples:0]
- 戻る (もどる) - [v1] to turn back [tier:core_n4] [examples:0]
- 申し上げる (もうしあげる) - [v2] to say; to offer [tier:core_n4] [examples:0]
- 申す (もうす) - [v1] to be called; to say [tier:core_n4] [examples:0]
- 迎える (むかえる) - [v2] to go out to meet [tier:core_n4] [examples:0]
- 向かう (むかう) - [v1] to head towards [tier:core_n4] [examples:0]
- 投げる (なげる) - [v2] to throw or cast away [tier:core_n4] [examples:0]
- 泣く (なく) - [v1] to weep [tier:core_n4] [examples:0]
- 無くなる (なくなる) - [v1] to disappear; to get lost [tier:core_n4] [examples:0]
- 亡くなる (なくなる) - [v1] to die [tier:core_n4] [examples:0]
- 直る (なおる) - [v1] to be fixed, to be repaired [tier:core_n4] [examples:0]
- 治る (なおる) - [v1] to be cured; to heal [tier:core_n4] [examples:0]
- 慣れる (なれる) - [v2] to get used to [tier:core_n4] [examples:0]
- 鳴る (なる) - [v1] to sound [tier:core_n4] [examples:0]
- 寝坊する (ねぼうする) - [v3] to sleeping in late [tier:core_n4] [examples:0]
- 眠る (ねむる) - [v1] to sleep [tier:core_n4] [examples:0]
- 逃げる (にげる) - [v2] to escape [tier:core_n4] [examples:0]
- 似る (にる) - [v2] to be similar [tier:core_n4] [examples:0]
- 残る (のこる) - [v1] to remain [tier:core_n4] [examples:0]
- 乗り換える (のりかえる) - [v2] to change between buses or trains [tier:core_n4] [examples:0]
- 濡れる (ぬれる) - [v2] to get wet [tier:core_n4] [examples:0]
- 塗る (ぬる) - [v1] to paint; to plaster [tier:core_n4] [examples:0]
- 盗む (ぬすむ) - [v1] to steal [tier:core_n4] [examples:0]
- 入学する (にゅうがくする) - [v3] to entry to school or university [tier:core_n4] [examples:0]
- 入院する (にゅういんする) - [v3] to hospitalization [tier:core_n4] [examples:0]
- 落ちる (おちる) - [v2] to fall or drop [tier:core_n4] [examples:0]
- 驚く (おどろく) - [v1] to be surprised [tier:core_n4] [examples:0]
- 踊る (おどる) - [v1] to dance [tier:core_n4] [examples:0]
- お出でになる (おいでになる) - [v1] (respectful) to be [tier:core_n4] [examples:0]
- お祝いする (おいわいする) - [v3] to congratulation [tier:core_n4] [examples:0]
- 行う (おこなう) - [v1] to perform; to do; to carry out [tier:core_n4] [examples:0]
- 怒る (おこる) - [v1] to be angry [tier:core_n4] [examples:0]
- 起こす (おこす) - [v1] to wake [tier:core_n4] [examples:0]
- 遅れる (おくれる) - [v2] to be late [tier:core_n4] [examples:0]
- 送る (おくる) - [v1] to send [tier:core_n4] [examples:0]
- 思い出す (おもいだす) - [v1] to remember [tier:core_n4] [examples:0]
- 折れる (おれる) - [v2] to break; to be broken [tier:core_n4] [examples:0]
- 下りる (おりる) - [v2] to get off [tier:core_n4] [examples:0]
- 折る (おる) - [v1] to break or to fold [tier:core_n4] [examples:0]
- 仰る (おっしゃる) - [v1] (respectful) to say [tier:core_n4] [examples:0]
- 落とす (おとす) - [v1] to drop [tier:core_n4] [examples:0]
- 冷房する (れいぼうする) - [v3] to air conditioning [tier:core_n4] [examples:0]
- 連絡する (れんらくする) - [v3] to contact [tier:core_n4] [examples:0]
- 利用する (りようする) - [v3] to use [tier:core_n4] [examples:0]
- 留守する (るすする) - [v3] to absence [tier:core_n4] [examples:0]
- 下がる (さがる) - [v1] to get down [tier:core_n4] [examples:0]
- 探す (さがす) - [v1] to look for [tier:core_n4] [examples:0]
- 下げる (さげる) - [v2] to lower [tier:core_n4] [examples:0]
- 差し上げる (さしあげる) - [v2] to give [tier:core_n4] [examples:0]
- 騒ぐ (さわぐ) - [v1] to make noise, to be excited [tier:core_n4] [examples:0]
- 触る (さわる) - [v1] to touch [tier:core_n4] [examples:0]
- 生活する (せいかつする) - [v3] to live [tier:core_n4] [examples:0]
- 生産する (せいさんする) - [v3] to production [tier:core_n4] [examples:0]
- 戦争する (せんそうする) - [v3] to war [tier:core_n4] [examples:0]
- 説明する (せつめいする) - [v3] to explanation [tier:core_n4] [examples:0]
- 試合する (しあいする) - [v3] to match, game [tier:core_n4] [examples:0]
- 叱る (しかる) - [v1] to scold [tier:core_n4] [examples:0]
- 試験する (しけんする) - [v3] to examination [tier:core_n4] [examples:0]
- 失敗する (しっぱいする) - [v3] to failure [tier:core_n4] [examples:0]
- 調べる (しらべる) - [v2] to investigate [tier:core_n4] [examples:0]
- 知らせる (しらせる) - [v2] to notify [tier:core_n4] [examples:0]
- 生じる (しょうじる) - [v2] to produce [tier:core_n4] [examples:0]
- 紹介する (しょうかいする) - [v3] to introduction [tier:core_n4] [examples:0]
- 育てる (そだてる) - [v2] to rear, to bring up [tier:core_n4] [examples:0]
- 卒業する (そつぎょうする) - [v3] to graduation [tier:core_n4] [examples:0]
- 相談する (そうだんする) - [v3] to discuss [tier:core_n4] [examples:0]
- 滑る (すべる) - [v1] to slide; to slip [tier:core_n4] [examples:0]
- 水泳する (すいえいする) - [v3] to swimming [tier:core_n4] [examples:0]
- 空く (すく) - [v1] to be hungry [tier:core_n4] [examples:0]
- 済む (すむ) - [v1] to finish [tier:core_n4] [examples:0]
- 進む (すすむ) - [v1] to make progress [tier:core_n4] [examples:0]
- 捨てる (すてる) - [v2] to throw away [tier:core_n4] [examples:0]
- 退院する (たいいんする) - [v3] to leaving hospital [tier:core_n4] [examples:0]
- 誕生する (たんじょうする) - [v3] to birth [tier:core_n4] [examples:0]
- 倒れる (たおれる) - [v2] to fall (over, down) [tier:core_n4] [examples:0]
- 足りる (たりる) - [v2] to be sufficient; to be enough [tier:core_n4] [examples:0]
- 足す (たす) - [v1] to add (numbers) [tier:core_n4] [examples:0]
- 建てる (たてる) - [v2] to build [tier:core_n4] [examples:0]
- 尋ねる (たずねる) - [v2] to ask [tier:core_n4] [examples:0]
- 訪ねる (たずねる) - [v2] to visit [tier:core_n4] [examples:0]
- 手伝う (てつだう) - [v1] to help; to assist; to aid [tier:core_n4] [examples:0]
- 届ける (とどける) - [v2] to send [tier:core_n4] [examples:0]
- 泊まる (とまる) - [v1] to stay at [tier:core_n4] [examples:0]
- 止める (とめる) - [v2] to stop something [tier:core_n4] [examples:0]
- 通る (とおる) - [v1] to go through [tier:core_n4] [examples:0]
- 取り替える (とりかえる) - [v2] to exchange; to swap [tier:core_n4] [examples:0]
- 続ける (つdずける) - [v2] to continue; to keep on [tier:core_n4] [examples:0]
- 続く (つdずく) - [v1] to continue [tier:core_n4] [examples:0]
- 捕まえる (つかまえる) - [v2] to catch [tier:core_n4] [examples:0]
- 漬ける (つける) - [v2] to soak; to pickle [tier:core_n4] [examples:0]
- 付く (つく) - [v1] to be attached [tier:core_n4] [examples:0]
- 連れる (つれる) - [v2] to take (someone) with one [tier:core_n4] [examples:0]
- 釣る (つる) - [v1] to fish [tier:core_n4] [examples:0]
- 伝える (つたえる) - [v2] to report; to tell [tier:core_n4] [examples:0]
- 包む (つつむ) - [v1] to wrap [tier:core_n4] [examples:0]
- 植える (うえる) - [v2] to plant; to grow [tier:core_n4] [examples:0]
- 動く (うごく) - [v1] to move [tier:core_n4] [examples:0]
- 伺う (うかがう) - [v1] to visit [tier:core_n4] [examples:0]
- 受ける (うける) - [v2] to take a lesson or test [tier:core_n4] [examples:0]
- 打つ (うつ) - [v1] to hit [tier:core_n4] [examples:0]
- 移る (うつる) - [v1] to move house or transfer [tier:core_n4] [examples:0]
- 写す (うつす) - [v1] to copy or photograph [tier:core_n4] [examples:0]
- 別れる (わかれる) - [v2] to separate [tier:core_n4] [examples:0]
- 沸かす (わかす) - [v1] to boil; to heat [tier:core_n4] [examples:0]
- 沸く (わく) - [v1] to boil [tier:core_n4] [examples:0]
- 笑う (わらう) - [v1] to laugh; to smile [tier:core_n4] [examples:0]
- 割れる (われる) - [v2] to break [tier:core_n4] [examples:0]
- 焼ける (やける) - [v2] to burn; to be roasted [tier:core_n4] [examples:0]
- 焼く (やく) - [v1] to bake; to grill [tier:core_n4] [examples:0]
- 役に立つ (やくにたつ) - [v1] to be helpful [tier:core_n4] [examples:0]
- 約束する (やくそくする) - [v3] to promise [tier:core_n4] [examples:0]
- 止む (やむ) - [v1] to stop [tier:core_n4] [examples:0]
- 痩せる (やせる) - [v2] to become thin [tier:core_n4] [examples:0]
- 汚れる (よごれる) - [v2] to get dirty [tier:core_n4] [examples:0]
- 喜ぶ (よろこぶ) - [v1] to be delighted [tier:core_n4] [examples:0]
- 寄る (よる) - [v1] to visit; to drop by [tier:core_n4] [examples:0]
- 予習する (よしゅうする) - [v3] to preparation for a lesson [tier:core_n4] [examples:0]
- 用意する (よういする) - [v3] to preparation [tier:core_n4] [examples:0]
- 予約する (よやくする) - [v3] to reservation [tier:core_n4] [examples:0]
- 揺れる (ゆれる) - [v2] to shake [tier:core_n4] [examples:0]

## 13. I-adjectives

- 浅い (あさい) - [i-adj] shallow [tier:core_n4] [examples:0]
- 深い (ふかい) - [i-adj] deep [tier:core_n4] [examples:0]
- 恥ずかしい (はずかしい) - [i-adj] embarrassed [tier:core_n4] [examples:0]
- 酷い (ひどい) - [i-adj] terrible; awful [tier:core_n4] [examples:0]
- 悲しい (かなしい) - [i-adj] sad [tier:core_n4] [examples:0]
- 硬い (かたい) - [i-adj] hard [tier:core_n4] [examples:0]
- 厳しい (きびしい) - [i-adj] strict [tier:core_n4] [examples:0]
- 細かい (こまかい) - [i-adj] small, fine [tier:core_n4] [examples:0]
- 怖い (こわい) - [i-adj] frightening [tier:core_n4] [examples:0]
- 珍しい (めずらしい) - [i-adj] unusual; rare [tier:core_n4] [examples:0]
- 眠い (ねむい) - [i-adj] sleepy [tier:core_n4] [examples:0]
- 苦い (にがい) - [i-adj] bitter [tier:core_n4] [examples:0]
- 可笑しい (おかしい) - [i-adj] strange or funny [tier:core_n4] [examples:0]
- 寂しい (さびしい) - [i-adj] lonely [tier:core_n4] [examples:0]
- 素晴らしい (すばらしい) - [i-adj] wonderful [tier:core_n4] [examples:0]
- 凄い (すごい) - [i-adj] terrific [tier:core_n4] [examples:0]
- 正しい (ただしい) - [i-adj] right; correct [tier:core_n4] [examples:0]
- 嬉しい (うれしい) - [i-adj] happy [tier:core_n4] [examples:0]
- 美しい (うつくしい) - [i-adj] beautiful [tier:core_n4] [examples:0]
- 優しい (やさしい) - [i-adj] kind [tier:core_n4] [examples:0]
- 柔らかい (やわらかい) - [i-adj] soft [tier:core_n4] [examples:0]

## 14. Na-adjectives

- 安心 (あんしん) - [na-adj] peace of mind [tier:core_n4] [examples:0]
- 安全 (あんぜん) - [na-adj] safety; security [tier:core_n4] [examples:0]
- 大事 (だいじ) - [na-adj] important; serious; crucial [tier:core_n4] [examples:0]
- 不便 (ふべん) - [na-adj] inconvenience [tier:core_n4] [examples:0]
- 複雑 (ふくざつ) - [na-adj] complexity; complication [tier:core_n4] [examples:0]
- 反対 (はんたい) - [na-adj] opposition [tier:core_n4] [examples:0]
- 変 (へん) - [na-adj] strange; peculiar; weird [tier:core_n4] [examples:0]
- 久しぶり (ひさしぶり) - [na-adj] after a long time [tier:core_n4] [examples:0]
- いっぱい (いっぱい) - [na-adj] full [tier:core_n4] [examples:0]
- 一生懸命 (いっしょうけんめい) - [na-adj] very hard; with utmost effort [tier:core_n4] [examples:0]
- 自由 (じゆう) - [na-adj] freedom [tier:core_n4] [examples:0]
- 十分 (じゅうぶん) - [na-adj] enough; sufficient; plenty [tier:core_n4] [examples:0]
- 簡単 (かんたん) - [na-adj] simple; easy [tier:core_n4] [examples:0]
- 危険 (きけん) - [na-adj] danger [tier:core_n4] [examples:0]
- 急 (きゅう) - [na-adj] sudden; abrupt; unexpected [tier:core_n4] [examples:0]
- 無理 (むり) - [na-adj] impossible [tier:core_n4] [examples:0]
- 盛ん (さかん) - [na-adj] popularity; prosperous [tier:core_n4] [examples:0]
- 親切 (しんせつ) - [na-adj] kindness [tier:core_n4] [examples:0]
- 楽しみ (たのしみ) - [na-adj] looking forward to [tier:core_n4] [examples:0]
- 丁寧 (ていねい) - [na-adj] polite [tier:core_n4] [examples:0]
- 適当 (てきとう) - [na-adj] suitable [tier:core_n4] [examples:0]
- 特別 (とくべつ) - [na-adj] special; particular [tier:core_n4] [examples:0]
- 残念 (ざんねん) - [na-adj] regrettable; unfortunate [tier:core_n4] [examples:0]

## 15. Adverbs

- ああ (ああ) - [adv.] ah; yes [tier:core_n4] [examples:0]
- びっくり (びっくり) - [adv.] to be surprised [tier:core_n4] [examples:0]
- 大分 (だいぶ) - [adv.] considerably; greatly; a lot [tier:core_n4] [examples:0]
- できるだけ (できるだけ) - [adv.] as much as possible [tier:core_n4] [examples:0]
- どんどん (どんどん) - [adv.] rapidly; more and more [tier:core_n4] [examples:0]
- はっきり (はっきり) - [adv.] clearly [tier:core_n4] [examples:0]
- 非常に (ひじょうに) - [adv.] extremely [tier:core_n4] [examples:0]
- ほとんど (ほとんど) - [adv.] mostly [tier:core_n4] [examples:0]
- 必ず (かならず) - [adv.] always; certainly [tier:core_n4] [examples:0]
- この間 (このあいだ) - [adv.] the other day; recently [tier:core_n4] [examples:0]
- このごろ (このごろ) - [adv.] these days; nowadays [tier:core_n4] [examples:0]
- こう (こう) - [adv.] this way [tier:core_n4] [examples:0]
- まず (まず) - [adv.] first of all [tier:core_n4] [examples:0]
- もし (もし) - [adv.] if; in case; supposing [tier:core_n4] [examples:0]
- もうすぐ (もうすぐ) - [adv.] soon [tier:core_n4] [examples:0]
- なるほど (なるほど) - [adv.] now I understand [tier:core_n4] [examples:0]
- 最近 (さいきん) - [adv.] recently [tier:core_n4] [examples:0]
- 最初 (さいしょ) - [adv.] beginning; first [tier:core_n4] [examples:0]
- 昨夜 (さくや) - [adv.] last night [tier:core_n4] [examples:0]
- 再来月 (さらいげつ) - [adv.] month after next [tier:core_n4] [examples:0]
- 再来週 (さらいしゅう) - [adv.] week after next [tier:core_n4] [examples:0]
- しっかり (しっかり) - [adv.] firmly; steadily [tier:core_n4] [examples:0]
- 将来 (しょうらい) - [adv.] future [tier:core_n4] [examples:0]
- それほど (それほど) - [adv.] to that extent [tier:core_n4] [examples:0]
- そろそろ (そろそろ) - [adv.] gradually; soon [tier:core_n4] [examples:0]
- すっかり (すっかり) - [adv.] completely [tier:core_n4] [examples:0]
- たいてい (たいてい) - [adv.] usually [tier:core_n4] [examples:0]
- たまに (たまに) - [adv.] occasionally [tier:core_n4] [examples:0]
- 途中 (とちゅう) - [adv.] on the way [tier:core_n4] [examples:0]
- 特に (とくに) - [adv.] especially; in particular [tier:core_n4] [examples:0]
- 到頭 (とうとう) - [adv.] finally; after all [tier:core_n4] [examples:0]
- やっぱり (やっぱり) - [adv.] as I thought [tier:core_n4] [examples:0]
- 全然 (ぜんぜん) - [adv.] not entirely (negative) [tier:core_n4] [examples:0]

## 16. Conjunctions

- これから (これから) - [conj.] after this [tier:core_n4] [examples:0]
- それで (それで) - [conj.] because of that [tier:core_n4] [examples:0]

## 17. Counters and quantities

(seed corpus has no entries for this section yet - extend from Tanos N4 in next pass)

## 18. Set phrases / expressions

- あ (あ) - [exp.] Ah; oh [tier:core_n4] [examples:0]

