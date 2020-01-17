#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<stddef.h>
#include<dirent.h>
#include<signal.h>
#include<stdlib.h>
#include<sys/stat.h>

int main(void)
{
//initialize variables
    int c;              //container
    int i=0;            //index
    char editor[255];   //editor location

//use a input window to get the input from user
//Two button user chooice set peference editor or not
    printf("<ibox:input weith = 300> <button {Set editor} onclick = <put{y:<ibox>*}>,ibox.clear>");
    printf("<button {Do not set} onclick = <put{n:<ibox>*}>>");

//a while loop to get the editor name
	while ((c = getchar())!='*')
	{
	editor[i] = c;
	i++;
	}

//clear window
printf("<program.clear>");

while (1)
{
	int i=0;                //index for getchar()
	int c=0;                //container for getchar()
	char n[255]="";            // contain anumber
	char dir[255]="";          // contain directory
	char buf[255]="";          // buffer
    char er[255] = "";      // contain error message
	char command[255] = "";

    //perset command
	char x[255] = "mate-terminal -x ./";
	char cat[255] = "mate-terminal -x less ";
	char file[] = "{</#x1F4C2>}";

    //get current directory
	getcwd(dir,sizeof(dir));

    //pint a box to create file
	printf("<ibox:input weith = 300> <button {creat new file} onclick = <put{n:<ibox>*}>,ibox.clear></n>");

    //print current directory
	printf("<cur_dir:box span size= 30 {Current working directory:}{<span size = 30 color = {orange} %s>}{%s}></n>",file,dir);

    //print go back button
	printf("<button {go back} onclick =<put {d:..*}>>");

    //print a button to edite file
	printf("<editor:button visible=false {edite} onclick = <put {^}>></n>");

    //a function whitch can print all file
	get_pwd_info();

    // a while loop to get a string whitch pushed by button
    // put the string in to command
	while ((c = getchar())!='*')
	{
	command[i] = c;
	i++;
	}
   
    //an option loop to judge the type of file that user chooiced
	if (command[0] == 'd')
	{
        //store file name into n
		strcpy(n,command+2);
		if (!(access(n,X_OK)))
		{
            //if user has permision then go to new directory
			strcat(dir,"/");
			strcat(dir,n);
			chdir(dir);
		}
		else
		{
            //if user has not permison print error message
			strcat(er,"Can't access ");
			strcat(er,n);
		}
	}

    // if the first character is x which means user want to execute some file
	if (command[0] == 'x')
	{
        
        //put file name to n
		strcpy(n,command+2);

        //judge whether uer has permision to execute file or not
		if (!(access(n,X_OK)))
		{

            // if user has perimision, execute the file in another window
			strcat(x,n);
			system(x);
		}
		else
		{
    
            // if user has not permision, print error message
			strcat(er,"Can't excute ");
			strcat(er,n);
		}
	}

    // if the first character of command is v, means user want to view a file
	if (command[0] == 'v')
	{

        //initializ variable to contain filename and buffer
		char filename[100]="";
		char buf[255]="";
		int size=0;

        //use stuct to judge the size of file
		struct stat finfo;
		strcat(buf,command+2);

        //get the size of file
		size = get_size(buf);

        //if size is too large, print error message
		if (size > 500)
			{
			strcat(er,"Error: Could not open text file. File szie too large.");
			}
		else

        //if size is less than 500kb,open file
			{
			strcat(cat,buf);
			system(cat);
			}

	}

    // if the first character is n which means user want to create new file
	if (command[0] == 'n')
	{

        //If the first character is y whitch means user have enter editor
        //use user peference editor to create new file
        if (editor[0] == 'y')
        {
        //set buffer to contain command
            char buf[255]="";

        //put the editor location to buffer
            strcat(buf,editor+2);
            strcat(buf," ");

        //put the file name to buffer
		    strcat(buf,command+2);

        //run command
		    system(buf);
        }

        //use default editor whitch is nano
        else
        {
            char nano[255] = "mate-terminal -x nano ";
            strcat(nano,command+2);
            system(nano);  
        }
    
	}

   
    //if the first character is e witch means user want to edit a file
	if (command[0] == 'e')
	{

    //make the editor button visible
        printf("<editor.visible true>");

    //put the file name to n
		strcat(n,command+2);

    //get the event witch is user enter edite
		c = getchar();

    //if user enter edite
		if (c == '^')
		{
    //If the first character is y whitch means user have enter editor
        //use user peference editor to create new file
        if (editor[0] == 'y')
        {
        //set buffer to contain command
            char buf[255]="";

        //put the editor location to buffer
            strcat(buf,editor+2);
            strcat(buf," ");
        //put the file name to buffer
		    strcat(buf,command+2);
		    system(buf);
            }

        //use default editor whitch is nano
            else
            {

        // use nano command and open new terminal to edite file
                char nano[255] = "mate-terminal -x nano ";
                strcat(nano,command+2);   
                system(nano);
            }
		}
	}

    //clear window
	printf("<program.clear>");

    //print error message
	printf("<box span size = 30 {Error message :%s}></n>",er);
}
}

//a function used get file size
int get_size(char *filename)
{

//use struct to get information of file
	struct stat statbuf;
	stat(filename,&statbuf);
	int size = statbuf.st_size;

//transferm size to kb
	size = size/1000;

//return the file size
	return size;
}

//a function used to print all file
int get_pwd_info()
{
    //set variable to contain pointer and set struct
	DIR *dir;
	struct dirent *ptr;
	int i;
	struct stat buf;

//use getcwd function and opendir function to get directory
//set a pointer n to contain name of file
	char pwd[255];
	char *n;

//get directory and put in dir
	getcwd(pwd,sizeof(pwd));
	dir = opendir(pwd);

// three icons code used to print icon
	char file[] = "{</#x1F4C2>}";
	char text[] = "{</#x1F5CE>}";
	char exe[] = "{</#x1F5B0>}";

//a while loop to print files 
	while((ptr = readdir(dir))!=NULL)
	{

//put file name into n
		n = ptr->d_name;
		stat(n,&buf);
		char m[255]="";

//saving file name and sticy a special symbol "*"
		strcat(m,n);
		strcat(m,"*");

// check whether is hidden file or not
		if(n[0]=='.')
		{
			continue;
		}

// if this file is direcotry, print a button with directory icons
		else if(S_ISDIR(buf.st_mode))
		{
			printf("<d:button height = 150 width = 300 border = 0 {< span size = 40 color = {blue} %s>} {</n>}{%s} onclick = <put {d:%s}> >",file,n,m);
		}

//if this file is executable, print a button with executable icons
		else if(!access(n,X_OK))
		{
			printf("<e:button height = 150 width = 300 border = 0 {< span size = 40 color = {green} %s>} {</n>} {%s} onclick = <put {x:%s}>>",exe,n,m);
		}

//if this file is txt, print the name of file with icon in a button
//also create right click event, if user right click a file then the edite button will become visible,and user can use it to edit file.
		else
		{
			printf("<v:button height = 150 width = 300 border = 0 {< span size = 40 color = {orange} %s>} {</n>} {%s} onclick = <put {v:%s}> oncontextclick = <put {e:%s}>>",text,n,m,m);
		}
	}
}

