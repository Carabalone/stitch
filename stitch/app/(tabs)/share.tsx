import React, { useEffect, useState } from 'react';
import { Text, View } from "react-native";
import { StatusBar } from "expo-status-bar";
import axios from 'axios';

export default function Test() {
  const [patientInfo, setPatientInfo] = useState(null);

  useEffect(() => {
    const apiUrl = 'http://194.210.210.197:5000';

    axios.get(apiUrl)
      .then(response => setPatientInfo(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <View className='flex-1 justify-center items-center bg-white'>
      <Text>Test Page</Text>
      {patientInfo ? <Text>{JSON.stringify(patientInfo)}</Text> : <Text>Loading...</Text>}
      <StatusBar style='auto' />
    </View>
  );
}
