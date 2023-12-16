def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    # TODO
    # ここにメール送信処理
    # scalesにレビュー予約情報が入っている → sample_as_reviewee.json参照(レビュワーとしてのサンプルレスポンスまだない)
    # slotsに自分の開けたスロット情報がはいっている。連続した時間帯でスロットいれても実際は15分長さで45分間隔になっている → sample_my_slots.json参照、サンプルは2023/12/17 16時~17時のスロットを開けています
    # me → sample_me.json参照
