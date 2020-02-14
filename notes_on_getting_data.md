
# QQ Dataset
[url](https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0)

Extracted via js with
```
// Areas

[...document.querySelectorAll('.placeItem.placeArea')].filter(el => el.querySelector('.confirm')).map(el => `${el.querySelector('h2').innerText},${el.querySelector('.confirm').innerText},${el.querySelector('.heal').innerText}, ${el.querySelector('.dead').innerText}`).join('\n')

// Cities
[...document.querySelectorAll('.placeItem.placeArea')].map(el => el.innerText).join('\n')
```

# DXY Dataset
[url](https://ncov.dxy.cn/ncovh5/view/pneumonia)

Extracted by copy-pasting the city breakdown (below the fold).
