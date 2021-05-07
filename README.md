# Information Security
(資訊安全導論實作作業 2021/03 ~)

## hw1: Classical Encryption Techniques (實作加密部分)
### Sample Input & Output
1. Autokey chipher: 每單筆測資輸入 2 行，第 1 行表示 Key K，第 2 行表示要被加密的字串 S，其中K、S 皆為大小寫英文字母所組成

<code>
  Input:\n
  deceptive\n
  wearediscoveredsaveyourself\n
  
  Output:
  zicvtwqngkzeiigasxstslvvwla
</code>

2. Rail Fence Cipher: 每單筆測資輸入 2 行，第 1 行表示 Key K，第 2 行表示要被加密的字串 S，其中1 < K < 256，S 為可視字元所組成

<code>
  Input:
  7
  https://www.youtube.com/watch?v=UHxSYMEqv1U&ab_channel=UnusualVideos
  
  Output:
  hywYhat.o/aSMcaultwumtxE_nsVpwtocHqbnuiswuchUvaend:/b.?=1&lUes/evU=o
</code>

3. Vigenère Cipher: 每單筆測資輸入 2 行，第 1 行表示 Key K，第 2 行表示要被加密的字串 S，其中K、S 皆為大小寫英文字母所組成

<code>
  Input:
  sesame
  thisisatestmessage
  
  Output:
  llasuwsxwsfqwwkasi
</code>

4. Caesar cipher: 設定key為9，不論輸入大小寫，輸出皆為小寫，非字母不做處理直接輸出

<code>
  Input:
  hellohowareyou
  
  Output:
  qnuuxqxfjanhxd
</code>

5. Playfair cipher: 第一行輸入為key，第二行為要被加密的字串，輸出一律為大寫

<code>
  Input:
  CATS
  TODAYISFRIDAY
  
  Output:
  CQECVMTGOMECZV
</code>

6. Row transposition: 第一行輸入為key，第二行為要被加密的字串，輸出一律為小寫，忽略空格

<code>
  Input:
  4312567
  attack postponed until two am xyz
  
  Output:
  ttnaaptmtsuoaodwcoixknlypetz
</code>

## hw2: DES (ECB mode) (實作解密部分)
每單筆測資會輸入 2 行，第一行表示 Key K (長度為 64 bits, 每個 Byte 的最後 1 bit 為 parity bits)，第二行表示密文 C
K 以 [0-9a-f] 組成, 共有 16 個字元, 每 2 個字元組成 1 個 Byte；C 為 [0-9a-f] 組成, 每 2 個字元組成 1 個 Byte

<code>
  Input:
  52415020474f4420
  b7625c9fe4cb43b3843b01843b62431e7fe4dcd031caabe23ec69c6f62c19df
  
  Output:
  I'm beginnin' to feel like a Rap God, Rap God
</code>
