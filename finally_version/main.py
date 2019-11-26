# 引入各自分析文件
import DSAL
import DSF
import ECO
import str_merge
import time

if __name__ == "__main__":
    r_ECO  = ECO.get_ECO()
    time.sleep(1)
    r_DSAL = DSAL.get_DSAL()
    time.sleep(1)
    r_DSF  = DSF.get_DSF()

    # print(r_ECO)
    # print(type(r_DSAL))
    # print(r_DSF)

    str_merge.merge("經濟局", r_ECO)
    str_merge.merge("勞工局", r_DSAL)
    str_merge.merge("財政局", r_DSF)