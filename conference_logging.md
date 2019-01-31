# How to take notes at a conference (or any event)


I have recently started attending scientific conferences
([ICLR](http://noecasas.com/post/iclr2018/),
[EAMT](http://noecasas.com/post/eamt2018/),
[EMNLP](http://noecasas.com/post/emnlp2018/)). I had the need to take notes of what I was learning, and to take pictures of posters and slides used during presentations and write down ideas that came to my mind.

Maybe there are better solutions out there, but I devised my own simple workflow. Here I explain it.

**Note**: many people live-tweet conferences. I like this approach as a means to share the contents of e.g. orals, but not for private notes (e.g. about ideas you had) and things you prefer to keep for yourself, which is the use case I cover here.

### Outline

This workflow relies on the instant messaging tool **whatsapp**.

It offers Android and iOs apps, as well as a web interface at https://web.whatsapp.com .

The workflow steps are to:

1. Create a whatsapp group 
2. Take pictures and quick notes on the go with the whatsapp mobile app.
3. Take notes via whatsapp web interface from your laptop.
4. After the conference, export the group's chat history via email.
5. Create a self-contained PDF with your notes and pictures.

### Create a whatsapp group for the conference

The idea is to create a whatsapp group where all notes and pictures will be sent to.

I normally create a group with myself alone. This can be achieved by creating a 2-person group and then expelling the other person.

You can also have other people participate in the group to collaboratively log the conference or simply monitor the stuff others post.

### Taking notes and pictures via the mobile app

When I'm at the poster sessions, I like taking pictures of the posters I find interesting, and sometimes I take notes of pieces of information the authors share with me while discussing their work, like how they are extending their algorithms in new directions or cases they found they algorithm not to work so well.

I also like to take pictures of interesting slides during the oral presentations of the conference.

For these cases (pictures and quick notes on the go), I use the whatsapp mobile app, sending everything to the group I created specifically for the conference.

### Taking notes via the web interface

Sometimes I can use the laptop, like during the oral presentations, invited talks or tutorials. In such cases, I open the whatsapp web interface and I use it to take notes, sending them as messages to the whatsapp group I created specifically for the conference.

While I take notes, I occasionally also use the mobile app to take pictures and post them to the same group, interleaving picture and explanation/idea.

### Export chat history

Once the conference has finished, I export the whatsapp group contents via email. To do so, open the group and, in the menu, select _More → Export Chat_, specify that you want the pictures to be saved along with the text, and send it via email to yourself.

The email you just sent yourself should have several attachments. These should include a text file plus the pictures you sent to the group. Whatsapp reduces the quality of the pictures, which is convenient because this way they fit more easily as attachments in the email. Note that this may not be convenient if you want very high-resolution pictures; for posters and slides this is no problem at all.

###  Create a beautiful PDF

Download all the attachments of the email to a local folder. Now use my wonderful script `whatsapp2md` to create a markdown file. You can find all the details about how to use it [here](https://github.com/noe/whatsapp2md).

Optionally, edit the markdown file as you please (e.g. adding some extra info, removing stuff) before the final step.

Finally, open the markdown file with your favourite viewer and print it to PDF to get a beautiful self-contained PDF that you can archive or share.

