const areas = {
  implementation: {label:'EVIDENCE INTO PRACTICE',title:'What helps better care<br>take root?',description:'Exploring how evidence becomes part of routine care, with attention to behavior, local context, and the systems in which change happens.',tags:['Behavioral science','Implementation theory']},
  decisions: {label:'PEOPLE AT THE CENTER',title:'What matters to the<br>person making the decision?',description:'Studying how evidence, clinical expertise, and individual priorities can come together in health decisions, including the role of decision support.',tags:['Shared decision making','Decision support']},
  cancer: {label:'ACROSS THE CARE JOURNEY',title:'How can evidence inform<br>the cancer care journey?',description:'Research interests include cancer screening and prehabilitation: connecting implementation questions with decisions before and during care.',tags:['Cancer screening','Prehabilitation']},
  methods: {label:'UNDERSTANDING CONTEXT',title:'What works, for whom,<br>and in what circumstances?',description:'Using realist approaches, mixed methods, and evidence synthesis to examine the interaction between people, interventions, and complex systems.',tags:['Realist approaches','Mixed methods','Evidence synthesis']}
};
const tabs = [...document.querySelectorAll('[role="tab"]')];
function selectArea(tab){
  tabs.forEach(t=>{const active=t===tab;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1;t.querySelector('.tab-plus').textContent=active?'−':'+';});
  const area=areas[tab.dataset.area];
  document.querySelector('#area-label').textContent=area.label;
  document.querySelector('#area-title').innerHTML=area.title;
  document.querySelector('#area-description').textContent=area.description;
  document.querySelector('#area-tags').replaceChildren(...area.tags.map(tag=>{const span=document.createElement('span');span.textContent=tag;return span;}));
  document.querySelector('#research-panel').setAttribute('aria-labelledby',tab.id);
}
tabs.forEach((tab,i)=>{
  tab.addEventListener('click',()=>selectArea(tab));
  tab.addEventListener('keydown',e=>{let next;if(e.key==='ArrowDown')next=(i+1)%tabs.length;if(e.key==='ArrowUp')next=(i-1+tabs.length)%tabs.length;if(e.key==='Home')next=0;if(e.key==='End')next=tabs.length-1;if(next!==undefined){e.preventDefault();selectArea(tabs[next]);tabs[next].focus();}});
});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
  const filter=button.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(b=>{const active=b===button;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
  let count=0;document.querySelectorAll('.publication').forEach(p=>{p.hidden=filter!=='all'&&p.dataset.topic!==filter;if(!p.hidden)count++;});
  document.querySelector('.result-count').textContent=`Showing ${count} selected publication${count===1?'':'s'}`;
}));
const menu=document.querySelector('.menu');const nav=document.querySelector('#nav');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');}
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus();}});
