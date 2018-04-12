%function send_trigger(p,trigger,dt)
% function send_trigger(p,trigger,dt)
%if(~exist('dt'))
 %dt = 0.004; %4ms
%end
%if p.usetrigs
% DaqDOut(p.di,0,trigger); %send trigger
% WaitSecs(dt);
% DaqDOut(p.di,0,0); %clear trig
%end