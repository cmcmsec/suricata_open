from django.shortcuts import render
from .models import SuriMonitor
import json
from django.http import HttpResponse
from django.db import connections

def rule(request):
    data={"flag_one":"suricata","flag_two":"rule"}
    return render(request, 'suricata/rule.html', data)


def monitor(request):
    sobjs = SuriMonitor.objects.filter(project="suricata")
    flag="new"

    data = {"flag_one": "suricata", "flag_two": "monitor","flag":flag}
    return render(request, 'suricata/monitor.html', data)

def edit_mornitor(request,suid):
    sobjs = SuriMonitor.objects.filter(project="suricata",id=suid)
    flag="edit"
    sobj=sobjs[0]
    data = {"flag_one": "suricata", "flag_two": "monitor","flag":flag,"sobj":sobj}
    return render(request, 'suricata/monitor.html', data)

def savesuri(request):
    sid=request.POST.get("sid")
    times = request.POST.get("times")
    cnts = request.POST.get("cnts")
    tips = request.POST.get("tips")
    flag = request.POST.get("flag")
    suid = request.POST.get("suid")
    #print(sid,times,cnts)
    code=0
    try:
        #SuriMonitor.objects.filter(project="suricata").delete()
        if flag=="edit":
            s = SuriMonitor.objects.filter(id=int(suid))[0]
        else:
            s = SuriMonitor()
        s.project="suricata"
        s.sid = int(sid)
        s.times = int(times)
        s.cnts = int(cnts)
        s.tips = tips
        s.save()
    except Exception as e:
        print(e)
        print("$$$$$$$$$$")
        code=1
    ret={"code":code}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")

def delmor(request,suid):

    print(suid)
    code=0

    if suid:
        aobj = sobjs = SuriMonitor.objects.filter(project="suricata",id=suid)

        aobj.delete()

    ret={"code":code}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")


def morlist(request):
    suriobjs = SuriMonitor.objects.filter(project="suricata")
    data = {"flag_one": "suricata", "flag_two": "morlist","suriobjs":suriobjs}
    return render(request, 'suricata/morlist.html', data)
def monitorSave(request):
    ret={"code":200}
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
    data = {}
    recode = data['recode']
    retdata = {}
    retdata["code"] = recode
    retdata["remsg"] = data['remsg']
    if recode == 0:
        robj = RedisHelper()
        for url in data["url_list"]:
            t = TaskInfo()
            t.command = data['task_command']
            t.url = url
            t.method = data['task_method']
            t.postdata = data['task_postdata']
            t.plugins = data['task_plugins']
            t.crawler = data['task_crawler']
            t.user = data['task_user']
            t.status=1
            t.save()
            tid = t.id
            tcrawf=False
            if data['task_crawler']=='1':
                tcrawf=True
            tmsg={}
            tmsg["taskid"]=str(tid)
            tmsg["user"] = data['task_user']
            tmsg["command"] = data['task_command']
            tmsg["url"] = url
            tmsg["request-method"] = data['task_method']
            tmsg["post-data"] = data['task_postdata']
            tmsg["plugins"] = data['task_plugins']
            tmsg["basic-crawler"] = tcrawf

            robj.pushTask(tmsg)

            print(tid)

    return HttpResponse(json.dumps(retdata, ensure_ascii=False), content_type="application/json,charset=utf-8")

