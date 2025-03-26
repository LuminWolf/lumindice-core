# log提取为csv

import re

import pandas as pd


def log2csv(log_path) -> pd.DataFrame:
    with open(log_path, "r", encoding="utf-8") as f:
        log = f.read()
    log = log.split('\n')
    df = pd.DataFrame(columns=["username", "speech"])
    start_idx = -1
    for idx, speech in enumerate(log):
        # 发言结束
        if speech == "":
            speech_list = log[start_idx + 1:idx]
            username = "ERROR"
            if len(speech_list) == 1:
                username = "SYSTEM"
            elif len(speech_list) > 1:
                match = re.match(username_pattern, speech_list[0])
                if match:
                    username = match.group(1)
            start_idx = idx
            temp = pd.DataFrame([[f"{username}", speech_list[1:]]],
                                columns=df.columns)
            df = pd.concat([df, temp], ignore_index=True)
    return df


if __name__ == '__main__':
    username_pattern = r"^\s*([^\(]+)\s*\("
    ooctalk_pattern = r"\(()\)"  # 未使用

    def main():
        # 预处理为csv
        log_path = r"G:\Favourite\跑团\COC\陵墓\log\g1026445942_1739359386.txt"
        csv_path = r"G:\Favourite\跑团\COC\陵墓\log\g1026445942_1739359386.csv"
        # log : pd.DataFrame = log2csv(log_path)
        # log.to_csv(csv_path, index=False, encoding="utf-8")

        # 个性化数据清洗
        dice_name = "我"
        kp_name = "TNT"
        df = pd.read_csv(csv_path, encoding="utf-8")
        print(df["speech"])


    main()
