# -*- coding: utf-8 -*-
"""

"""
import os
from traits.api import HasTraits, Str, Directory, Bool, Button,Int
from traitsui.api import View, Item, Group
from traitsui.menu import CancelButton
import traitsui
from traitsui.message import message, error,auto_close_message
import argparse
from shutil import copy
import datetime
from getpass import getuser
import subprocess
import time

class subject(HasTraits):
    if os.path.exists(os.environ['SUBJECTS_DIR']):
        project_surface_directory= Directory(os.environ['SUBJECTS_DIR'],mandatory=True, desc="project's surface directory")
    else:
        project_surface_directory= Directory(mandatory=True, desc="project's surface directory")
    subject_id=Str(mandatory=True)
    subjects_existence=Bool
    check_for_subjects_surfaces = Button(label="Check for subject's surface")
    date=datetime.date.today().strftime("%m_%d_%Y")
 
###Subject Info tab   
    def _check_for_subjects_surfaces_fired(self):
        project_surface_directory=self.project_surface_directory
        subject_id=self.subject_id
        os.environ['SUBJECTS_DIR']=self.project_surface_directory
        if os.path.isfile(os.path.join(project_surface_directory,subject_id,
                                       'mri','aparc+aseg.mgz')):
            self.subjects_existence=True
            message(message='Subject %s was successfully found at %s.'%(subject_id,os.path.join(project_surface_directory,subject_id)),title='Subject successfully found', buttons=['OK'])
        else:
            self.subjects_existence=False 
            error(message='Subject %s was not found at %s. Please check your subject directory and subject id'%(subject_id,os.path.join(project_surface_directory,subject_id)), title='Subject not found', buttons=['OK'])
      
###Editing Subject tab
      
    Editing_message='Not all buttons are necessary for all subjects. Please see documentation for more information.'
    
    
    view_subject= Button(action='view_subject',label = 'view subject')
    def _view_subject_fired(self):
        sp=os.path.join(self.project_surface_directory,self.subject_id)
        print sp
        os.environ['SUBJECTS_DIR']=self.project_surface_directory
        if not os.path.exists(os.path.join(sp,'tmp','control.dat')):           
            #os.system('echo "1.0 0 10" >> %s/tmp/control.dat'%(sp))
            os.system('touch %s/tmp/control.dat'%(sp))
        os.system('freeview -viewport y -v %s/mri/T1.mgz \
                %s/mri/brainmask.mgz \
                %s/mri/wm.mgz:colormap=heat:opacity=.4 \
                -f %s/surf/lh.white:edgecolor=blue \
                %s/surf/lh.pial:edgecolor=cyan \
                %s/surf/rh.white:edgecolor=blue \
                %s/surf/rh.pial:edgecolor=cyan -c %s/tmp/control.dat'%(sp,sp,sp,sp,sp,sp,sp,sp))
        if not os.path.exists(os.path.join(sp,'edit.log')):
            auto_close_message(message='Editing log started for %s on %s'%(self.subject_id,time.strftime("%Y_%b_%d_%H%M",time.localtime())),time=3.0,title='Message')
            os.system('echo "Editing Log for subject %s started on %s" >> %s'%(self.subject_id,time.strftime("%Y_%b_%d_%H%M",time.localtime()), os.path.join(sp,'edit.log')))
            
    rate_the_brain=Int(mandatory=False, label='Rate the Brain for motion')
    
    watershed = Button(action='watershed',label = 'Adjusting the Watershed Threshold')
    watershed_threshold=Int(25,mandatory=True,desc='watershed threshold')    
    def _watershed_fired(self):
        sp = os.path.join(self.project_surface_directory,self.subject_id)
        if not os.path.exists(os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date)):        
            copy(os.path.join(sp,'mri','brainmask.mgz'),os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date))
            os.system('backup of brainmask made on %s >> %s'%(self.date,os.path.join(sp,'edit.log')))   
        os.system('recon-all -skullstrip -wsthresh %s -clean-bm -no-wsgcaatlas -subjid %s'%(self.watershed_threshold,self.subject_id))
        os.system('echo "skullstripping with watershed threshold level %s was run on %s" >> %s'%(self.watershed_threshold,time.strftime("%Y_%b_%d_%H%M",time.localtime()),os.path.join(sp,'edit.log')))
    
    gcuts = Button(action = 'gcuts',label = 'Run gcuts')
    def _gcuts_fired(self):
        sp = os.path.join(self.project_surface_directory,self.subject_id)
        if os.path.exists(os.path.join(sp,'mri','brainmask.braincuts.mgz')):
            message(message='gcuts has already been run for subject %s'%self.subject_id)
        else:
            if not os.path.isfile(os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date)):
                copy(os.path.join(sp,'mri','brainmask.mgz'),os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date))
            os.system('recon-all -skullstrip -clean-bm -gcut -subjid %s'%self.subject_id)
            os.system('echo "gcuts was run on %s" >> %s' %(time.strftime("%Y_%b_%d_%H%M",time.localtime()),os.path.join(sp,'edit.log')))
            
    view_gcuts = Button(action = 'view_gcuts', label = 'View gcuts effect')
    def _view_gcuts_fired(self):
        sp = os.path.join(self.project_surface_directory,self.subject_id)
        os.system('freeview -viewport y -v %s/mri/brainmask.mgz \
                  %s/mri/T1.mgz \
                  %s/mri/brainmask.gcuts.mgz:colormap=heat:opacity=.5'%(sp,sp,sp))
    
    wm_pial_edits=Button(action='wm_pial_edits',label = 'Control point and WM editing')
    
    def _wm_pial_edits_fired(self):
        sp=os.path.join(self.project_surface_directory,self.subject_id)
        if not os.path.isfile(os.path.join(sp,'tmp','control.dat')):           
            #os.system('echo "1.0 0 10" >> %s/tmp/control.dat'%(sp))
            os.system('touch %s/temp/control.dat'%(sp))
        os.system('echo "WM and control point edits were made on %s" >> %s'%(time.strftime("%Y_%b_%d_%H%M",time.localtime()),os.path.join(sp,'edit.log')))
        if not os.path.isfile(os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date)):
            copy(os.path.join(sp,'mri','brainmask.mgz'),os.path.join(sp,'mri','brainmask_backup_%s.mgz'%self.date))
            os.system('echo "backup of brainmask made on %s" >> %s'%(time.strftime("%Y_%b_%d_%H%M",time.localtime()),os.path.join(sp,'edit.log')))
        if not os.path.isfile(os.path.join(sp,'mri','wm_backup_%s.mgz'%self.date)):
            copy(os.path.join(sp,'mri','wm.mgz'),os.path.join(sp,'mri','wm_backup_%s.mgz'%self.date))
            os.system('echo "backup of white matter mask made on %s" >> %s'%(time.strftime("%Y_%b_%d_%H%M",time.localtime()), os.path.join(sp,'edit.log')))
        
        os.system('freeview -viewport y -v %s/mri/T1.mgz \
                %s/mri/brainmask.mgz \
                %s/mri/wm.mgz:colormap=heat:opacity=.4 \
                -f %s/surf/lh.white:edgecolor=blue \
                %s/surf/lh.pial:edgecolor=cyan \
                %s/surf/rh.white:edgecolor=blue \
                %s/surf/rh.pial:edgecolor=cyan -c %s/tmp/control.dat'%(sp,sp,sp,sp,sp,sp,sp,sp))
        if not os.path.isfile(os.path.join(sp,'edit.log')):
            auto_close_message(message='Editing log started for %s on %s'%(self.subject_id,self.date),time=3.0,title='Message')
    recon_message='Run the recons separately. If you have done edits to both, run control points first.' 

    run_wm_recon = Button(action='run_wm_recon',label = 'Recon white matter edits')
    def _run_wm_recon_fired(self):
        sp=os.path.join(self.project_surface_directory,self.subject_id)
        os.system('echo "wm reconstruction run on %s" >> %s'%(datetime.date.today().strftime("%c"),os.path.join(sp,'edit.log')))
        os.system('recon-all -autorecon2-wm -autorecon3 -subjid %s'%self.subject_id)        
    
    run_cp_recon = Button(action='run_cp_recon', label = 'Recon control point edits')
    def _run_cp_recon_fired(self):
        sp=os.path.join(self.project_surface_directory,self.subject_id)
        os.system('echo "cp reconstruction run on %s" >> %s'%(datetime.date.today().strftime("%c"),os.path.join(sp,'edit.log')))
        os.system('recon-all -autorecon2-cp -autorecon3 -subjid %s'%self.subject_id)   
        
    check_on_jobs = Button(action='check_qsub', label = 'Check on my current recon jobs')
    def _check_on_jobs_fired(self):
        user=getuser()
        recon_jobs=subprocess.check_output("qstat -u %s | grep 'recon'"%user,shell = True)
        message(message='%s'%recon_jobs)
    
    # Additional_Notes=Str
    # #additional_notes_file=os.path.join(project_surface_directory,subject_id,'edit_additional_notes.log')
    # if os.path.exists(os.path.join(project_surface_directory,subject_id,'edit_additional_notes.log')):
    #     file=open(additional_notes_file,'r')
    #     Additional_Notes=[]
    #     for row in file:
    #         Additional_Notes.extend(row)
    #     file.close()
    # save_additional_notes=Button(action='save_additional_notes', label='Save Notes')

    # def _save_additional_notes_fired(self):
        
    #     if not os.path.exists(additional_notes_file):
    #         additional_notes_file=os.path.join(project_surface_directory,subject_id,'edit_additional_notes.log')
    #         os.system('touch %s'%additional_notes_file)
    #     os.system('echo %s > %s'%(self.Additional_notes,additional_notes_file))
    #     message(message='Additional notes file saved.',title='Save Notes Completed')

    
###Documentation/help tab    
    view_bert = Button(action= 'view_bert', label='view example subject')
    def _view_bert_fired(self):
        bp=os.path.join(os.environ['FREESURFER_HOME'],'subjects','bert')
        os.system('freeview -viewport y -v %s/mri/T1.mgz \
                %s/mri/brainmask.mgz \
                %s/mri/wm.mgz:colormap=heat:opacity=.4 \
                -f %s/surf/lh.white:edgecolor=blue \
                %s/surf/lh.pial:edgecolor=cyan \
                %s/surf/rh.white:edgecolor=blue \
                %s/surf/rh.pial:edgecolor=cyan '%(bp,bp,bp,bp,bp,bp,bp))

    open_gablab_documentation= Button(action='open_qlab_documentation',label = 'view qlab documentation')
    def _open_gablab_documentation_fired(self):
        os.system('open -a "Google Chrome" https://github.com/Qlab-UDel/qlab/wiki/FreeSurfer-Overview')
        
    open_documentation = Button(action='open_documentation', label = 'view Freesurfer documentation')
    def _open_documentation_fired(self):
        os.system('open -a "Google Chrome" http://freesurfer.net/fswiki/Edits')    
        
        
view1 = View(Group(Item(name = 'project_surface_directory'),
                   Item(name = 'subject_id'),
                   Item(name = 'check_for_subjects_surfaces', show_label= False),                   
                   label='Subject information'),
             Group(Item(name='Editing_message',show_label=False,style='readonly'),
                        Group(Item(name = 'view_subject', show_label=False,tooltip='This will view your subject'),label='Viewing the subject', show_border=True),
                              Group(Group(Item(name = 'watershed', show_label=False, tooltip='this will adjust the watershed value for skullstripping'),
                                          Item(name= 'watershed_threshold', show_label=True, tooltip='Watershed threshold'),orientation = 'horizontal'),
                               Group(Item(name= 'gcuts', show_label=False, tooltip=' This will run gcuts, which is an automated process for a finer skull strip, always check results'),
                                     Item(name='view_gcuts', show_label = False, tooltip='Visualize the effect of running gcuts'),orientation='horizontal'),
                                label = 'Skullstripping',orientation = 'vertical', show_border=True),

                         Group(Item(name='wm_pial_edits',show_label=False,tooltip='Launches the subject and relevant surfaces in freeview'),
                               Group(Item(name='recon_message',show_label=False,style='readonly'),
                                     Group(Item(name='run_cp_recon',show_label = False, tooltip = 'Runs the recon for control point edits'),
                                           Item(name='run_wm_recon', show_label = False, tooltip = 'Runs the recon for white matter edits'), orientation='horizontal'),
                                            show_border = False, orientation = 'vertical'),                         
                         label='White Matter and Control Point Editing',show_border=True),
                         Item(name='check_on_jobs',show_label=False,tooltip = 'check on current recon jobs'),
                         label='Editing Brain Actions',
                         orientation='vertical', layout='normal',show_labels=True),
                        #Item(name='Additional_notes',show_label=True),
                        #orientation='horizontal',layout='split',show_border='True'),
             Group(Item(name = 'view_bert', show_label=False,tooltip='This example subject of bert, located in the freesurfer directory. This is a provided example of an edited brain'),
                   Item(name = 'open_gablab_documentation', show_label=False, tooltip='This documentation was put together by Nayeon Kim, and others'),
                   Item(name = 'open_documentation',show_label= False, tooltip='This documentation is provided by the Freesurfer people'),
                   orientation='horizontal',layout='normal',show_border=True,
                   label='View Documentation/help'),
                   resizable=True,
                   buttons=[CancelButton])
                   #width=500)

if __name__ == "__main__":
    subject_view = subject()
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '-subjid', dest='subject_id', help='subject_id to edit')
    args = parser.parse_args()    
    if args.subject_id != '':
        subject_id=args.subject_id
    subject_view.configure_traits(view=view1)

        
