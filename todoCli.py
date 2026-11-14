import argparse
from taskTracker import add_task,del_task,update_task,filter_list


parser = argparse.ArgumentParser(prog='task CLI')
subparser = parser.add_subparsers(dest='commands',required=True)

# Add SubParser
parser_add = subparser.add_parser("add",help="Adding a Task")
parser_add.add_argument("Description",help="Description of the Task")
parser_add.add_argument("-p","--Progress",help='Markling a Task',choices=["Mark-in-progress","Mark-in-done"],default="Mark-in-progress")

#Del SubParser
parser_del = subparser.add_parser("del",help="Deleting Task by ID")
parser_del.add_argument("id",help="Enter Id you want to delete",type=int)


#Update SubParser
parser_update = subparser.add_parser("update",help="Ypdating task by ID")
parser_update.add_argument("id",help="Enter ID you want to update",type=int)
parser_update.add_argument("-D","--Updated_Description",help="Udpate the Desciption")
parser_update.add_argument("-P","--Updated_Progress",help="Update The Progress",choices=["In-Future","Halt","Mark-in-done"])


#List SubParser
parser_list = subparser.add_parser("list",help="Show all the List")
parser_list.add_argument("-id","--id",help="Enter ID you want to update",type=int)
parser_list.add_argument("-p","--Progress",help="Enter a Description of Progress to see",choices=["Mark-in-progress","Mark-in-done","In-Future","Halt"])

args = parser.parse_args()

if args.commands == 'add':
    add_task(args.Description,args.Progress)
elif args.commands == 'del':
    del_task(args.id)
elif args.commands == 'update':
    update_task(args.id,args.Updated_Description,args.Updated_Progress)
elif args.commands == 'list':
    filter_list(args.id,args.Progress)