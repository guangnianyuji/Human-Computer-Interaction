# Documentation

## 1 Project Requirements

Design the interface for a floor navigation mobile app for the 4th floor of the Jishi Building, presented in a visual format while adhering to the principles of fluid navigation.

The app should fulfill the following requirements:

1. Provide an overview of all rooms on the 4th floor of the Jishi Building.
2. Allow users to quickly select and view specific rooms.
3. Support keyword search (e.g., search for "Student Affairs Office" or "Grace").

## 2 Design Overview

### 2.1 Splash Screen

![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab4/pagepicture/%E5%BC%80%E5%B1%8F.png?raw=true)

This is the splash screen of the app, which briefly indicates that it is a navigation app for the 4th floor of the Jishi Building at Tongji University's School of Software Engineering. The core concept of the design is "Seek what you seek."

### 2.2 Home Page

 ![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab4/pagepicture/%E4%B8%BB%E9%A1%B5.png?raw=true)

This is the home page of the app.

First, I have designed and implemented support for room keyword search, which will be explained in the next section.

Second, following the principle of presenting attractive choices using graphical techniques in fluid navigation, I have provided an overall floor plan of the 4th floor of the Jishi Building. This is an intuitive navigation method for users. They can click on specific locations on the map, and the corresponding room number label will appear. Clicking again will navigate them to the respective room. The map is clear and room labels are visible, enabling users to accurately click on the desired room's location.

Third, following the principle of organizing menu items by categories and ensuring understandable meanings in fluid navigation, I have designed a list that includes all the rooms and supports category-based searches. The categories are as follows:

```
| 所有
| 教研室
| 会议室
| 办公室
├ 实验室
   | 机房
   | 工作室
   | 学科实验室
 
```

This organization allows users to search for rooms based on specific categories. I have ensured that each room in the list has a clear identifier and recognizable name for quick browsing and selection by the users.

### 2.3 Search Page

![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab4/pagepicture/%E6%90%9C%E7%B4%A2.png?raw=true)

I have designed the ability for users to quickly find the room they need by entering the room name or keywords. It ensures that relevant room information is displayed in the search results, enabling users to easily select the correct room.

Additionally, I have designed the display of recent search records on the search page. This helps users quickly select previously searched rooms, avoiding the need to re-enter the same keywords and allowing them to directly click and find the desired room. A clear button is provided for users to easily delete unwanted search records.

### 2.4 Room Details Page

![](https://github.com/guangnianyuji/Human-Computer-Interaction/blob/main/Lab4/pagepicture/%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF.png?raw=true)

I have designed the room details page to include a "Return to Home" button, allowing users to navigate back to the home page from the room details page. The button is located in the top-left corner of the page, making it easy to find and access, ensuring a consistent navigation experience.

The room details page includes the following information:

- Sliding window display of room photos, allowing users to visually understand the appearance and environment of the room. Users can easily switch and browse different photos within the sliding window.
- Room tags and related personnel: Each room is provided with tags indicating its functions and relevant personnel. Function tags can describe the purpose, characteristics, or category of the room. Information about related personnel facilitates communication and consultation when needed.
- Room information board: By displaying the information board installed near the entrance of each room, the reliability of the information is enhanced, and more detailed information is provided. The information board for laboratories includes contact numbers of the responsible persons, enabling users to communicate and consult when needed.

Additionally, I have designed an input box for user feedback, allowing users to provide feedback, especially when they discover incorrect room information or the need for updates. Such a feature helps improve the accuracy and timeliness of room information.