from fasthtml.common import *
from tasks_data import data, status_dd, priority_dd
from fh_frankenui.components import *
from fasthtml.svg import *

hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css"),)

app = FastHTML(hdrs=hdrs,debug=True,default_hdrs=False)

hotkeys = (('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team',''),('Logout',''))
avatar_opts =Ul(cls='uk-dropdown-nav uk-nav')(
                            Li(cls='px-2 py-1.5 text-sm')(
                                Div(cls='flex flex-col space-y-1')(
                                    P('sveltecult', cls='text-sm font-medium leading-none'),
                                    P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'))),
                            Li(cls='uk-nav-divider'),
                            *map(lambda x: Li(A(cls='uk-drop-close justify-between')(x[0],Span(x[1],cls='ml-auto text-xs tracking-widest opacity-60'))), hotkeys))

def MakeTaskForm():
    return Form(cls='uk-modal-body uk-modal-dialog space-y-6')(
             UkH3('Create Task'),P(cls=TextT.muted_sm)('Fill out the information below to create a new task',),
             Div(cls='grid grid-cols-3 gap-2')(
               UkSelect(*map(Option,('Documentation','Bug','Feature')),                  label='Task Type',id='task_type'),
               UkSelect(*map(Option,('In Progress','Backlog','Todo','Cancelled','Done')),label='Status',   id='task_status'),
               UkSelect(*map(Option,('Low','Medium','High')),                            label='Priority', id='task_priority')),
             UkTextArea(label='Title',placeholder='Please describe the task that needs to be completed'),
             Div(cls='grid grid-cols-2')(
                UkButton(cls=UkButtonT.ghost   + ' uk-modal-close')('Cancel'),
                UkButton(cls=UkButtonT.primary + ' uk-modal-close')('Submit')))

def UkIconButton(*c, cls='uk-icon-button-sm'): return Button(cls='uk-icon-button ' + stringify(cls))(*c)



@app.get('/')
def homepage():

    def CreateTaskModal():
        return Modal(
            Div(cls='p-6')(
                UkModalTitle('Create Task'),P(cls=TextT.muted_sm)('Fill out the information below to create a new task'),Br(),
                Form(cls='space-y-6')(
                    Div(cls='grid grid-cols-3 gap-2')(
                        UkSelect(*map(Option, ('Documentation', 'Bug', 'Feature')), label='Task Type', id='task_type'),
                        UkSelect(*map(Option, ('In Progress', 'Backlog', 'Todo', 'Cancelled', 'Done')), label='Status', id='task_status'),
                        UkSelect(*map(Option, ('Low', 'Medium', 'High')), label='Priority', id='task_priority')),
                    UkTextArea(label='Title', placeholder='Please describe the task that needs to be completed'),
                    Div(cls='flex justify-end space-x-2')(
                        UkButton(cls=UkButtonT.ghost + ' uk-modal-close')('Cancel'),
                        UkButton(cls=UkButtonT.primary + ' uk-modal-close')('Submit')))),
            id='TaskForm')

    page_heading =Div(cls='flex items-center justify-between space-y-2')(
                Div(cls='space-y-2')(
                    UkH2('Welcome back!'),P("Here's a list of your tasks for this month!", cls=TextT.muted_sm)),
                Div(A(href='#', cls='h-8 w-8 inline-flex rounded-full bg-accent ring-ring')(Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed=sveltecult')),
                    Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(avatar_opts)))
    
    table_controls =(UkInput(cls='w-[250px]',placeholder='Filter task'),
                     UkDropdownButton(label = "Status", options = [map(Span, (a['status'], a['count'])) for a in status_dd],
                         btn_cls=(TextT.medium_xs, 'uk-button-default'),dd_cls='flex justify-between capitalize'),
                     UkDropdownButton( label = "Priority", options = [map(Span, (a['priority'], a['count'])) for a in priority_dd],
                         btn_cls=(TextT.medium_xs,'uk-button-default'), dd_cls='flex justify-between capitalize'),
                    UkDropdownButton(label='View', options = [Div(cls='flex flex-column')((Span(o), Span(uk_icon='check'))) for o in ['Title','Status','Priority']],
                        btn_cls=(TextT.medium_xs,'uk-button-default')),
                    UkButton('Create Task',cls=('uk-button-primary', TextT.medium_xs), uk_toggle="target: #TaskForm"))
    
    return CreateTaskModal(),Div(cls='p-8')(
            page_heading,
        Div(cls='mt-8 flex items-center justify-between')(
                 Div(cls='flex flex-1 gap-4')(table_controls)),
             Div(cls='uk-overflow-auto mt-4 rounded-md border border-border')(
                 Table(cls='uk-table uk-table-middle uk-table-divider uk-table-hover uk-table-small')(
                     # Table header
                     Thead(Tr(Th(cls='uk-table-shrink p-2')(Input(type='checkbox', cls='uk-checkbox')),
                             *[Th(cls='p-2')(o) for o in ['Task','Title','Status','Priority']],
                             Th(cls='uk-table-shrink p-2'))),
                     # Table Body (Tasks content)
                     Tbody(
                         *[Tr(cls=a['selected'])(
                             Td(cls='uk-table-shrink p-2')(CheckboxX(cls='uk-checkbox')), 
                             Td(a['id'], cls='p-2'), # task id
                             Td(cls='uk-table-expand max-w-[500px] truncate p-2')(Span(a['label'], cls='uk-label capitalize'),Span(a['title'], cls='font-medium')),
                             *map(lambda x: Td(cls='uk-text-nowrap p-2 uk-text-capitalize')(x), (a['status'],a['priority'])) ,
                             Td(cls='p-2')(
                                 UkIconButton(cls='uk-icon-button-xsmall')(Span(uk_icon='more', cls='text-gray-400')),
                                 Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(
                                     Ul(cls='uk-dropdown-nav uk-nav')(
                                         *map(lambda x: Li(A(x, cls='uk-drop-close justify-between')), ('Edit','Make a copy','Favorite', ('Delete',Span('⌘⌫', cls='ml-auto text-xs tracking-widest opacity-60'))))))))
                           for a in data])),
             # Table Footer
             Div(cls='mt-4 flex items-center justify-between px-2')(
                 Div('1 of 100 row(s) selected.', cls='flex-1 text-sm text-muted-foreground'),
                 Div(cls='flex flex-none items-center space-x-8')(
                     Div('Page 1 of 10', cls='flex w-[100px] items-center justify-center text-sm font-medium'),
                     Div(cls='flex items-center space-x-2')(
                         # chevron navigation (dbl left, left, right, dbl right)
                         UkIconButton(cls='hidden lg:inline-flex')(Span('Go to last page', cls='sr-only'),
                             Span(uk_icon='chevron-double-left', cls='h-4 w-4')),
                         UkIconButton(Span('Go to previous page', cls='sr-only'),
                             Span(uk_icon='chevron-left', cls='h-4 w-4')),
                         UkIconButton(Span('Go to next page', cls='sr-only'),
                             Span(uk_icon='chevron-right', cls='h-4 w-4')),
                         UkIconButton(cls='hidden lg:inline-flex')(
                             Span('Go to last page', cls='sr-only'),
                             Span(uk_icon='chevron-double-right', cls='h-4 w-4')))))))
serve()
