import nltk
text=('动物 只要 不患 疾病 ， 食物 充足 ， 就 会 快乐 满足 。 人 也 应该 如此 ； 然而 现实 并非 这样 ， 至少 在 大多数 情况 下 并非 这样 。 假如 你 是 不幸 的 ， 你 或许 就 会 承认 ， 自己 在 这 一方面 并 不是 个 例外 。 假如 你 是 幸福 的 ， 请 自问 一下 ， 你 的 朋友 中有 几个 是 幸福 的 。 当 你 对 自己 的 朋友 作 了 一番 评论 之后 ， 你 就 应该 学会 察言观色 之术 ， 使 自己 更 善于 感受 日常生活 中 所 遇到 的 人们 的 各种 情绪 。 布莱克 说 ：')
fdist = nltk.FreqDist(text)


print (fdist.keys())

