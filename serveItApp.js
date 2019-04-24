
deployedurl='https://script.google.com/macros/s/AKfycby52onY9OX3abTGB9D3pPxm90a0qdEU13nSyC2iPisSbE_XCV0/exec'  PLEASE UPDATE WITH YOUR DEPLOYED URL!

function doGet(e) {
  url=e.queryString
  text=' '
  if (url=='https://arxiv.org/rss/physics.optics'){
    text=UrlFetchApp.fetch(url)}
  return  ContentService.createTextOutput(text)
}