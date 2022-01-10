// 항목 추가
const addbtn = document.querySelector("#add-btn")

addbtn.addEventListener("click", function () {
  let inputVal = document.querySelector("input")

  if (inputVal.value != "") {
    let ul = document.querySelector("ul")
    let li = document.createElement("li")

    li.innerHTML = '<input type="checkbox">' + inputVal.value
    ul.appendChild(li)

    inputVal.value = "" // 입력창 비우기
  }
})

// 전체 삭제
const clearbtn = document.querySelector("#del-all")

clearbtn.addEventListener("click", function () {
  let ul = document.querySelector("ul")
  ul.innerHTML = ""
})

// 마지막 삭제
const lastbtn = document.querySelector("#del-last")

lastbtn.addEventListener("click", function () {
  let ul = document.querySelector("ul")
  let last_li = ul.lastChild

  last_li.remove()
})
