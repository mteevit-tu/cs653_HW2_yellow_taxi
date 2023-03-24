# Homework 2: Amazon S3 Select with Taxi Trip Data
Instructions:
ให้น.ศ. เขียน python script hw2_xxxx.py ซึ่งใช้ AWS SDK for Python (Boto3) เพื่อ
สร้าง Amazon S3 bucket ชื่อ nyctlc-cs653-xxxx โดยแทน xxxx ด้วยเลข 4 ตัวท้ายของรหัสน.ศ. ของตัวเอง 
นำเข้าข้อมูล NYC TLC trip data (จาก https://registry.opendata.aws/nyc-tlc-trip-records-pds/)  ที่เกี่ยวข้องเข้า Bucket ที่สร้างไว้ในข้อ 1) 
query ข้อมูลด้วย Amazon S3 select เพื่อตอบคำถามต่อไปนี้
ในเดือน Jan 2017 มีจำนวน yellow taxi rides ทั้งหมดเท่าไร แยกจำนวน rides ตามประเภทการจ่ายเงิน (payment)
ในเดือน Jan 2017 Yellow taxi rides ในแต่ละจุดรับผู้โดยสาร (Pickup location) เป็นจำนวน rides มากน้อยเท่าไร และมีค่าโดยสารรวมของ rides และจำนวนผู้โดยสารเฉลี่ยต่อ rides ในแต่ละจุดเท่าไร 
ในเดือน Jan - Mar 2017 มีจำนวน yellow taxi rides ทั้งหมดเท่าไร แยกจำนวน rides ตามประเภทการจ่ายเงิน (payment)
หมายเหตุ: หลังทำการบ้านเสร็จ น.ศ.ควรลบทรัพยากรที่ไม่ใช้แล้วด้วยค่ะ

สิ่งที่ต้องส่งในกล่องบน courseweb รายวิชา
ไฟล์ PDF ซึ่งมี
ชื่อและนามสกุล และรหัสประจำตัวน.ศ. 
คำอธิบายการทำงานของ hw2_xxxx.py 
ภาพหน้าจอที่แสดงให้เห็น s3 bucket nyc-tlc-cs653-xxxx ต้องเห็นชื่อ bucket และข้อมูลข้างใน bucket
ภาพแสดงผลการรัน query ใน code และคำตอบที่ได้สำหรับ a) - c)
การสะท้อนการเรียนรู้ของน.ศ.จากการบ้านครั้งนี้
เราได้ความรู้และทักษะอะไรจากการทำการบ้านครั้งนี้บ้าง และคิดว่านำไปใช้ประโยชน์อย่างไรได้บ้าง
สิ่งที่เราชอบและไม่ชอบในการทำการบ้านครั้งนี้
คิดว่าตัวเองควรปรับปรุงอย่างไร หรือ มีอะไรอย่างอื่นที่ควรได้รับการปรับปรุงสำหรับการบ้านครั้งต่อไป
URL ของไฟล์ hw2_xxxx.py ที่ commit ไว้ใน github repo ส่วนตัวของน.ศ. ซึ่งเปิดให้อาจารย์ (rattanat@gmail.com) และ TA (ta1tonkit@gmail.com) สามารถเข้าถึงได้
***ระมัดระวังอย่าใส่ AWS credential ไว้บนไฟล์ใดๆ ของ repo เด็ดขาด***

Link ที่อาจจะเป็นประโยชน์ในการทำการบ้านนี้
https://github.com/aws-samples/cloud-experiments/tree/master/experiments/notebooks/exploring-data
https://aws.amazon.com/blogs/storage/querying-data-without-servers-or-databases-using-amazon-s3-select/ 
