import asyncio,sys
from playwright.async_api import async_playwright
U="http://localhost:8765";O="/workspace/loanapp/shots/gc/optA4-";SHOT=len(sys.argv)>1
async def state(pg,tag,w,shot=None):
  bt=pg.locator(".ab-iq:visible").nth(1)
  if await bt.get_attribute("aria-expanded")!="true": await bt.click()
  await pg.wait_for_timeout(300)
  p=pg.locator("#"+await bt.get_attribute("aria-controls"))
  r=await p.evaluate("p=>({as:!!p.querySelector('.iq-as:not([hidden])'),txt:(p.querySelector('.iq-as')||{}).innerText||'',who:!!p.querySelector('.iq-who:not([hidden])'),chk:!!p.querySelector('.chk:not([hidden])')})")
  print(w,tag,r)
  if shot and SHOT:
    await p.evaluate("p=>p.scrollIntoView({block:'center'})");await pg.screenshot(path=O+shot)
  return bt
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--headless=new"])
    for w in (390,1280):
      c=await b.new_context(viewport={"width":w,"height":860});posts=[]
      async def rt(r):
        if r.request.url.startswith(U): await r.continue_()
        elif r.request.method=="POST": posts.append(r.request.post_data[:0]+r.request.url[:30]); await r.fulfill(status=200,body="ok")
        else: await r.abort()
      await c.route("**/*",rt);pg=await c.new_page();errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
      await pg.goto(U+"/promos/")
      # open an inquiry BEFORE unlocking (common real path), then close it
      bt=await state(pg,"before-unlock",w);await bt.click()
      await pg.wait_for_selector("#ab-pop:not([hidden])",timeout=12000)
      await pg.wait_for_timeout(3200)
      await pg.fill("#ab-name","Juan Dela Cruz");await pg.fill("#ab-mobile","09171234567");await pg.fill("#ab-email","juan@example.com");await pg.check("#ab-consent")
      await pg.click("#ab-btn");await pg.wait_for_timeout(1500)
      print(w,"stored",await pg.evaluate("localStorage.getItem('promos_contact')"),"unlocked",await pg.evaluate("document.documentElement.classList.contains('ab-open')"))
      if await pg.locator("#ab-pop:not([hidden])").count(): await pg.keyboard.press("Escape")
      if SHOT:
        await pg.evaluate("document.querySelector('#xpander').scrollIntoView()");await pg.screenshot(path=O+f"{w}-promos-unlocked-collapsed.png")
      await state(pg,"same-session",w,f"{w}-promos-form-sending-as.png")
      await pg.reload();await pg.wait_for_timeout(500);await state(pg,"after-reload",w)
      q=await c.new_page();q.on("pageerror",lambda e:errs.append(str(e)));await q.goto(U+"/cars/xpander/");await q.wait_for_timeout(400)
      await q.locator(".vp-tg").first.click();await q.wait_for_timeout(300)
      bt=q.locator(".vp-b.open .ab-iq");await bt.click();await q.wait_for_timeout(300)
      r=await q.evaluate("()=>{var p=document.querySelector('.vp-b.open .iq-p');return {as:!!p.querySelector('.iq-as:not([hidden])'),who:!!p.querySelector('.iq-who:not([hidden])')}}");print(w,"car-page",r)
      if SHOT: await bt.evaluate("b=>b.scrollIntoView({block:'start'})");await q.evaluate("scrollBy(0,-90)");await q.screenshot(path=O+f"{w}-car-form-sending-as.png")
      print(w,"errs",errs,"posts(intercepted)",posts)
    await b.close()
asyncio.run(main())
