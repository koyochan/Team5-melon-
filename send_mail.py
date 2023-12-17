def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    
    # scalesからプロジェクト名を抽出
    project_names = []
    for scale in scales:
        if 'team' in scale and 'project_gitlab_path' in scale['team']:
            project_path = scale['team']['project_gitlab_path']
            project_name = project_path.split('/')[-1]
            project_names.append(project_name)

    # プロジェクト名のリストを確認するための出力（デバッグ用）
    print("プロジェクト名:", project_names)
    
    # TODO: ここにメール送信処理を実装
