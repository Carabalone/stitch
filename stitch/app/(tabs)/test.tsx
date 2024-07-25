import { Text, View } from "react-native";
import { StatusBar } from "expo-status-bar";

export default function test() {
  return (
    // <View style={styles.container}>
    <View className='flex-1 justify-center items-center bg-white'>
      <Text>Test Page</Text>
      <StatusBar style='auto' />
    </View>
  );
}

