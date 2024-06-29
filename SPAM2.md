# SPAM


## <a name="SPAM更改">SPAM更改</a>

### 対応概要
AI基盤の保守期限到来に伴い、システム更改を実施。
プリンシプルのB象限であること、AI第6世代では占有区画で構築する必要があること、現状のElcaroを継続して利用する場合、ライセンス費用が高額になることを踏まえ、SWA基盤へ移行しデータベースはSWA Aurora(Postgres互換)に変更する。

### スケジュール
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       対応スケジュール
    axisFormat  %y-%m
    tickInterval    1month

    予備検討    :done,  t1, 2023-09-01, 2024-01-31
    基本設計    :done,  t2, after t1,   2024-03-31
    詳細設計    :done,  t3, after t2,   2024-05-31
    IT          :active,t4, after t3,   2024-06-30
    ST          :       t5, after t4,   2024-08-31
    UAT         :       t6, after t5,   2024-10-31
    リリース    :milestone, t7, 2025-01-15, 0d
```

### 進捗概要
- 韓国法規制対応については、SWA-会社直契約のCustomer Agreementに対する追加契約(Addendum)を締結予定。
- Master CSP Assessment reportについては、東京リージョンを利用する場合は**利用出来ない**ことを法律事務所のアドバイザリーよりコメントあり。


## <a name="XIFプロトコル対応">XIFプロトコル対応</a>

### 対応概要
Vitinifer, SBEの取引IFで利用しているFOTプロトコルのEOLに伴い、後継となるプロトコルであるXIFプロトコルへの対応を行うもの。
香港拠点については、今次対応にて3rdパーティの取引ソースにも対応する。

### スケジュール
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       対応スケジュール
    axisFormat  %y-%m
    tickInterval    1month

    予備検討    :done,  t1, 2023-09-01, 2024-01-31
    基本設計    :done,  t2, after t1,   2024-03-31
    詳細設計    :done,  t3, after t2,   2024-05-31
    IT          :active,t4, after t3,   2024-06-30
    ST          :       t5, after t4,   2024-08-31
    UAT         :       t6, after t5,   2024-10-31
    リリース    :milestone, t7, 2025-01-15, 0d
```

### 進捗概要
- 6月よりMasked XXX serviceにより、実取引のXIFプロトコルデータをUAT環境にIF開始。
- 3rd party sourceについては、六月末よりIF開始予定。


