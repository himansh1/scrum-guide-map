'use strict';
const topics=JSON.parse(document.getElementById('canvas-topics').textContent);
const viewport=document.getElementById('viewport'),world=document.getElementById('world'),zoomLabel=document.getElementById('zoom-level'),jump=document.getElementById('branch-jump');
let view={x:0,y:0,scale:1},activeTopic=topics[0].id,paintPending=false,dragged=false;
const pointers=new Map();let gesture=null;
const clamp=(v,min,max)=>Math.max(min,Math.min(max,v));
function anchoredZoom(v,next,point){next=clamp(next,.02,3);const ratio=next/v.scale;return {x:point.x-(point.x-v.x)*ratio,y:point.y-(point.y-v.y)*ratio,scale:next};}
function paint(){if(paintPending)return;paintPending=true;requestAnimationFrame(()=>{paintPending=false;world.style.transform=`translate(${view.x}px,${view.y}px) scale(${view.scale})`;zoomLabel.textContent=Math.round(view.scale*100)+'%';});}
function zoom(next,point={x:viewport.clientWidth/2,y:viewport.clientHeight/2}){view=anchoredZoom(view,next,point);paint();}
function selectTopic(id){activeTopic=id;document.querySelectorAll('[data-topic-button]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.topicButton===id)));const topic=topics.find(t=>t.id===id);jump.replaceChildren(new Option('Jump within '+topic.label.toLowerCase()+'…',''),...topic.branches.map(t=>new Option(t.title,t.id)));}
function worldPosition(el){let x=0,y=0;for(let p=el;p&&p!==world;p=p.offsetParent){x+=p.offsetLeft;y+=p.offsetTop;}return {x,y};}
function focusElement(el){const topic=el.closest('[data-topic]');if(topic&&activeTopic!==topic.dataset.topic)selectTopic(topic.dataset.topic);const scale=clamp((viewport.clientWidth-20)/(topic?.offsetWidth||420),.2,1.35),column=worldPosition(topic||el),target=worldPosition(el);view={scale,x:10-column.x*scale,y:14-target.y*scale};paint();}
function focusId(id){focusElement(document.getElementById(id));}
function overview(){const scale=clamp((viewport.clientWidth-20)/world.offsetWidth,.02,1);view={scale,x:10,y:12};paint();}
function resize(){viewport.style.height=Math.max(200,window.innerHeight-document.querySelector('.controls').offsetHeight)+'px';}
function localPoint(e){const r=viewport.getBoundingClientRect();return {x:e.clientX-r.left,y:e.clientY-r.top};}
function beginGesture(){const ps=[...pointers.values()];gesture={view:{...view},points:ps.map(p=>({...p}))};}
viewport.addEventListener('pointerdown',e=>{if(e.pointerType==='mouse'&&e.button!==0)return;if(e.target.closest('a,button,select'))return;pointers.set(e.pointerId,localPoint(e));viewport.setPointerCapture(e.pointerId);dragged=false;beginGesture();viewport.classList.add('dragging');});
viewport.addEventListener('pointermove',e=>{if(!pointers.has(e.pointerId)||!gesture)return;const point=localPoint(e);pointers.set(e.pointerId,point);const ps=[...pointers.values()];if(ps.length===1){const dx=ps[0].x-gesture.points[0].x,dy=ps[0].y-gesture.points[0].y;dragged ||= Math.hypot(dx,dy)>6;view={...gesture.view,x:gesture.view.x+dx,y:gesture.view.y+dy};}else{const [a,b]=gesture.points,[c,d]=ps;if(!b)return;const startDistance=Math.hypot(b.x-a.x,b.y-a.y)||1;const distance=Math.hypot(d.x-c.x,d.y-c.y);const startMid={x:(a.x+b.x)/2,y:(a.y+b.y)/2},mid={x:(c.x+d.x)/2,y:(c.y+d.y)/2};view=anchoredZoom(gesture.view,gesture.view.scale*distance/startDistance,startMid);view.x+=mid.x-startMid.x;view.y+=mid.y-startMid.y;dragged=true;}paint();});
function endPointer(e){pointers.delete(e.pointerId);if(pointers.size)beginGesture();else{gesture=null;viewport.classList.remove('dragging');}}
viewport.addEventListener('pointerup',endPointer);viewport.addEventListener('pointercancel',endPointer);viewport.addEventListener('lostpointercapture',e=>{if(pointers.has(e.pointerId))endPointer(e);});
viewport.addEventListener('wheel',e=>{e.preventDefault();if(e.ctrlKey||e.metaKey)zoom(view.scale*Math.exp(-e.deltaY*.01),localPoint(e));else{view.x-=e.deltaX;view.y-=e.deltaY;paint();}},{passive:false});
viewport.addEventListener('dblclick',e=>{if(e.target.closest('a'))return;zoom(view.scale*1.5,localPoint(e));});
viewport.addEventListener('keydown',e=>{const moves={ArrowLeft:[80,0],ArrowRight:[-80,0],ArrowUp:[0,80],ArrowDown:[0,-80]};if(moves[e.key]){e.preventDefault();view.x+=moves[e.key][0];view.y+=moves[e.key][1];paint();}else if(e.key==='+'||e.key==='='){e.preventDefault();zoom(view.scale*1.25);}else if(e.key==='-'){e.preventDefault();zoom(view.scale/1.25);}else if(e.key==='Home'){e.preventDefault();focusId('c-'+activeTopic);}});
document.getElementById('zoom-in').addEventListener('click',()=>zoom(view.scale*1.3));document.getElementById('zoom-out').addEventListener('click',()=>zoom(view.scale/1.3));document.getElementById('fit-topic').addEventListener('click',()=>focusId('c-'+activeTopic));document.getElementById('overview').addEventListener('click',overview);
document.querySelectorAll('[data-topic-button]').forEach(b=>b.addEventListener('click',()=>{selectTopic(b.dataset.topicButton);focusId('c-'+activeTopic);b.scrollIntoView({block:'nearest',inline:'nearest'});}));
jump.addEventListener('change',()=>{if(jump.value)focusId(jump.value);});
window.addEventListener('resize',()=>{resize();focusId('c-'+activeTopic);});
resize();selectTopic(activeTopic);requestAnimationFrame(()=>focusId('c-'+activeTopic));
if('serviceWorker'in navigator&&location.protocol!=='file:')navigator.serviceWorker.register('./sw.js').catch(()=>{});
